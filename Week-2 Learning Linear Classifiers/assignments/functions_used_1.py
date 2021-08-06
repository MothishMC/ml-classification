def get_numpy_data(data_frame, features, label):
            ## INDEPENDENT FEATURES
    data_frame['intercept'] = 1
    features       = ['intercept'] + features
    features_frame = data_frame[features]
    feature_matrix = features_frame.to_numpy()  
            ## DEPENDENT FEATURES
    label_array  = data_frame[label]
    label_array  = label_array.to_numpy()  
    return(feature_matrix, label_array)

def predict_probability(feature_matrix , coefficients):
    score = np.dot(feature_matrix , coefficients)
    predictions = (1 / (1 + np.exp(-score)))
    return predictions

def feature_derivative(errors, feature):
    derivative = np.dot(errors,feature)
    return derivative 

def compute_log_likelihood(feature_matrix, sentiment, coefficients):
    indicator = (sentiment==+1)
    scores = np.dot(feature_matrix , coefficients)
    lp = np.sum((indicator - 1) * scores - np.log(1. + np.exp(-scores)))
    return lp

def logistic_regression(feature_matrix, sentiment, initial_coefficients, step_size, max_iter):
    coefficients = np.array(initial_coefficients)
    for itr in range(max_iter):
        predictions = predict_probability(feature_matrix , initial_coefficients)
        indicator   = sentiment==+1
        errors      = indicator - predictions

        ## Going through all the coefficients in every iterations

        for j in range(len(coefficients)):
            derivative      = feature_derivative(errors, feature_matrix[:,j])
            coefficients[j] = coefficients[j] + step_size * derivative
            
        if (itr <= 15) or (itr <= 100 and itr % 10 == 0) or (itr <= 1000 and itr % 100 == 0) \
        or (itr <= 10000 and itr % 1000 == 0) or (itr % 10000 == 0):
            lp = compute_log_likelihood(feature_matrix, sentiment, coefficients)
            print('iteration %*d: log likelihood of observed labels = %.8f' % \
                (int(np.ceil(np.log10(max_iter))), itr, lp))
    return coefficients 

def predict_sentiments(scores):
    if scores>0:
        predict_label = 1
    else:   
        predict_label = -1
    return predict_label
import pandas as pd
corpus = ["This is totally fine",
          "It is extremely awesome",
          "Very boring class"]

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()

x = cv.fit(corpus)   # learn the vocabularies 

# dictionary of words and their corresponding indices (arranged in alphabetical order)
print("Vocabulary")
print(x.vocabulary_) 

print("Feature Names")
print(cv.get_feature_names()) # list of volcabularies

print("awesome word is found in the vector : ",cv.transform(['awesome']).toarray())

x = cv.transform(corpus)  # transforms the matrix into document_term_matrix

print('The shape of the document term matrix    : ',x.shape)     # row --> 3(number of documents) and column --> 10(number of unique words)
print('The array format of document term matrix : ')
print(x.toarray())
print('The non-zero values occurs in the indices: ')
print(x)   # Will print in which [i,j] there are non-zero values 

## To represent the document-term matrix in a data-frame
df=pd.DataFrame(x.toarray(),columns = cv.get_feature_names())
print(df)
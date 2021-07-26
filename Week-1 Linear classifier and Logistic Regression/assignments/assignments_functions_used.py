def remove_punctuation(text):
    ## if the above punctuations are present it will be removed and replaced with NaN values
    mapping = str.maketrans(' ' , ' ' , string.punctuation)
    return text.translate(mapping)
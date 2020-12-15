import pandas as pd
import numpy as np

df=pd.read_csv('spam',sep='\t',names=['Status' , 'Message'])

total = len(df)
print('Total number of records : ',total)

spam = len(df[df['Status']=='spam'])
print('Spam Mails     : ',spam)
print('Non-Spam Mails : ',total-spam)

# Changing the Spam -> 0
# and Non-spam(ham) -> 1

# df.loc[df['Status']=='spam']=1 --> Will change the entire row value=1
# The below one will change the row with only 'Status' column and not the 'Message column'
df.loc[df['Status']=='spam',"Status",]  = 0
df.loc[df['Status']=='ham',"Status",] = 1

x = df[["Status"]]
y = df[["Message"]]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=4)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
x  = cv.fit_transform(['Hi Hello','Good morning','Hi Good'])
print(x.toarray())
print(cv.get_feature_names())  # total number of words in the list

# ['good', 'hello', 'hi', 'morning'] -> This is the squential order
# In the sentences where-ever the word appears it counts 1 else 0

# Now, lets check with our data-set
cv1 = CountVectorizer()
x_traincv  =cv1.fit_transform(x_train)
a          = x_traincv.toarray()



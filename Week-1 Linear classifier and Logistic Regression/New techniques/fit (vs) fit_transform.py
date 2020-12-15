import pandas as pd
df=pd.read_csv('Datapreprocessing.csv')

#print(df.isnull().sum())

from sklearn.impute import SimpleImputer
imp = SimpleImputer(missing_values=np.nan,strategy='mean')

imp.fit(df[['Age','Salary']])   
x = imp.transform(df[['Age','Salary']])   

imp.fit_transform(df[['Age','Salary']])
###########################################################
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(df['Country'])  # This only fits into the model
print(le.classes_) # ['Brazil' 'England' 'Germany' 'India' 'Poland' 'Spain']

# Now only the model is tranformed into the numbers which is further used in fitting other models
le.transform(df['Country']) # [4 5 2 5 2 4 3 4 3 4 0 5 2 5 2 0 5 1 2 1]
#######################################################
    
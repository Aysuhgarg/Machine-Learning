import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset =  pd.read_excel('sal1.xlsx',names=['age',
                               'workclass',
                               'fnlwgt',
                               'education',
                               'education-num',
                               'marital-status',
                               'occupation',
                               'relationship',
                               'race',
                               'gender',
                               'capital-gain',
                               'capital-loss',
                               'hours-per-week',
                               'native-country',
                               'salary'],na_values=' ?')
X = dataset.iloc[:,0:14].values
#temp = pd.DataFrame(X)
y = dataset.iloc[:,-1].values
#temp1 = pd.DataFrame(y)
dataset.isnull().sum()

test= pd.DataFrame(X[:,[1,6,13]])
test[0].value_counts()
test[0] = test[0].fillna(' Private')
test[0].value_counts()

test[1].value_counts()
test[1] = test[1].fillna(' Prof-specialty')
test[1].value_counts()

test[2].value_counts()
test[2] = test[2].fillna(' United-States')
test[2].value_counts()
X[:,[1,6,13]] = test
#A=pd.DataFrame(X)
#A.isnull().sum()


from sklearn.preprocessing import LabelEncoder
lab = LabelEncoder()

X[:,1] = lab.fit_transform(X[:,1])
X[:,3] = lab.fit_transform(X[:,3])
X[:,5] = lab.fit_transform(X[:,5])
X[:,6] = lab.fit_transform(X[:,6])
X[:,7] = lab.fit_transform(X[:,7])
X[:,8] = lab.fit_transform(X[:,8])
X[:,9] = lab.fit_transform(X[:,9])
X[:,13] = lab.fit_transform(X[:,13])


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

Dataset = pd.read_csv('Data.csv')
X = Dataset.iloc[:,:-1].values
Y = Dataset.iloc[:,3].values
#from sklearn.impute import SimpleImputer
#imputer= SimpleImputer(missing_values = 'NaN', strategy = 'mean', axis= 0)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values= np.NAN, strategy= 'mean', fill_value=None, verbose=0, copy=True)
imputer = ip=imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])
print(X)
print(Y)
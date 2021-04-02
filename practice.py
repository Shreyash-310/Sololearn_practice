# compare machine learning algorithms on the sonar classification dataset
import pandas as pd
from pandas import read_csv
from pycaret.classification import setup
from pycaret.classification import compare_models
df = pd.read_csv('sonar.csv', header = None)
n_col = df.shape[1]
df.columns = [str(i) for i in range(n_col)]
print(df.head())
print(df.shape)
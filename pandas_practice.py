# easiest way to create a dataframe is using dictionary.
import pandas as pd

data = {
    'ages': [14, 18, 24, 22],
    'heights': [165, 180, 176, 184]
}
df = pd.DataFrame(data)
#print(df)
# we can access a row using its index and the loc[] function:
#print(df[['ages', 'heights']])
#print(df.iloc[:3])
print(df[(df['ages'] > 18) | (df['heights'] > 180)])
print(df.head(2))
df.drop('ages', axis=1, inplace=True)
print(df)
"""axis=1 specifies that we want to drop a column. axis=0 will drop a row."""
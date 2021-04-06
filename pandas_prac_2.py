import pandas as pd
import matplotlib.pyplot as plt
# df['month'] = pd.to_datetime(df['date'],format="%d.%m.%y").dt.month_name()
data = {
    'width': [2, 2, 7, 1, 9],
    'height': [3, 1, 4, 6, 2]
}
df = pd.DataFrame(data)
# print(df)
df['area'] = df['width'] * df['height']
print(df)
df[['area', 'width', 'height']].plot()
#print(df.describe())
"""df.groupby('month')['cases'].sum()  # groupby month wise based on cases
df['cases'].sum()"""
print(df[df['area'] > 25])
print(df.groupby('area')['height'].max())
"""import pandas as pd
data = {
    'a': [1, 2, 3],
    'b': [5, 8, 4]
}
df = pd.DataFrame(data)
df['c'] = df['a']+df['b']
print(df.iloc[2]['c'])"""

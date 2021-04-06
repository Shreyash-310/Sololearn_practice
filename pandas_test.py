import pandas as pd
import  matplotlib.pyplot as plt
"""data = {
    'date': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'cases': [10, 12, 15, 19, 21, 36, 41, 16, 32, 29],
    'deaths': [2, 6, 8, 1, 6, 11, 12, 7, 9, 6]
}
df = pd.DataFrame(data)
# print(df)
df['ratio'] = df['deaths'] / df['cases']
max_ratio = df.loc[df["ratio"] == df["ratio"].max()]
print(max_ratio)"""

data = {
    'sport': ["Soccer", "Tennis", "Soccer", "Hockey"],
    'players': [5, 4, 8, 20]
}
df = pd.DataFrame(data)
print(df)
plt.pie(data['players'], labels=data['sport'])
plt.show()
df.groupby('sport')['players'].sum().plot(kind="pie")
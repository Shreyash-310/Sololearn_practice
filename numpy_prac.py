#print('hello world!')
import numpy as np
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
x = np.mean(players)
print(x)
y = np.std(players)
print(y)
a = x+y
b = x-y
"""c = []
for i in range(len(players)):
    if b < players[i] < a:
        c.append(players[i])
    else:
        continue
print(len(c))"""
count = len([v for v in players if b < v < a])
print(count)
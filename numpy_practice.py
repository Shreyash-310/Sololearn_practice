import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000,
                 230000, 280000, 290000, 300000, 500000, 420000, 100000,
                 150000, 280000])
a = len(data)

x = np.mean(data)
y = np.std(data)

count = int(len([i for i in data if (x - y) < i < (x + y)]))
print((count / a) * 100)

# getting the percentage of houses comes inside one standard deviation of mean

# finding the largest character
txt = input()
# print(txt)
t = txt.split()
# print(t)
A = []
for i in range(len(t)):
    a = len(t[i])
    A.append(a)
# print(A)
z = max(A)
y = A.index(z)
# print(y)
print(t[y])
"""t = ['all','is','well']
x = (t.index('well'))
print(x)"""

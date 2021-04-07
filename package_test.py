"""a = 'this'
b = 'is'
#c = 'great'
d = 'too!'
var4 = "-".join([a, b, c, d])
print(var4)
"""
"""str = ('a','b','c','d','e')
var1 = str(0)
var2 = str(1)
var3 = str(2)
var4 = str(3)
var5 = str(4)
var = "-".join([var1, var2, var3, var4, var5])
print(var)"""

# solution

def words(*args):
    x = "-".join(args)
    print(x)

words('a', 'b', 'c', 'd', 'e', 'f')

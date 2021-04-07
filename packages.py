"""def function(named_arg, *args):
    print(named_arg)
    print(args)
function(1, 2, 3, 4, 5)"""

"""def function(x, y, food="spam"):
    print(food)
function(1, 2)
function(1, 2, "egg")"""

"""def my_func(x, y=7, *args, **kwargs):
    print(args)         #  return a list
    print(kwargs)       #  return a dict
my_func(2, 3, 4, 5, 6, a=7, b=8)"""

"""# Tuple unpacking
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)"""

"""x, y =[1, 2]
x, y = y, x
print(y)"""

"""a, b, *c, d =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)"""

"""# ternary operator
a = 7
b = 1 if a >= 5 else 42
print(b)"""


def function():
    print("This is a module function")


if __name__ == "__main__":
    print("This is a script")

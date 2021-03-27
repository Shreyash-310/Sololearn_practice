"""def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5
print(apply_twice(add_five, 0))
"""
# pure function = Pure functions have no side effects, and return a value that depends only on their arguments.
# not easy to write
"""def pur_func(x,y):
    temp = x + 2*y
    return temp / (2*x + y)
# impure function
some_list = []
def impure(arg):
    some_list.append(arg)"""


# lambda function :- anonymous functions are called lambda function (single line of code)
"""def my_func(f, arg):
    return f(arg)
y = my_func(lambda x: 2 * x * x, 5)
print(y)"""

# lambda example
print((lambda x: x**2 + 5*x +4)(3))
double = lambda x: x*2
print(double(7))
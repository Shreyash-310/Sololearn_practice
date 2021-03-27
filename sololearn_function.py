#range(10,20,3)

"""def my_func():
    print("Spam")
    print("Spam")
    print("Spam")
my_func()"""

"""def print_with_word(word):
    print('Hello',word+'!')
print_with_word('SHree')
print_with_word('eggs')
print_with_word('spam')"""

"""def function(variable):
    variable+=1
    print(variable)
function(7)
print(variable)"""

"""def max(x,y):
    if x>=y:
        return x
    else:
        return y
print(max(5,8))
z = max(7,3)
print(z)"""

"""def print_numbers():
    print(1)
    print(2)
    return
    print(4)
    print(6)
print_numbers()"""

"""def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(x,y),func(x,y)

a=5
b=10
print(do_twice(add,a,b))"""

def square(x):
    return x*x
def test(func,x):
    print(func(x))

#print(square(10))
test(square,42)
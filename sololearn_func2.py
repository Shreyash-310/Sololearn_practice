# The function map takes a function and an iterable as arguments,
# and returns a new iterable with the function applied to each argument
"""def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)"""

# The function filter filters an iterable by removing items that don't match
# a predicate
"""nums = [11, 22, 33, 44, 55, 66]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)"""

# Generators
"""def countdown():
    i=5
    while i>0:
        yield i     # convert them into generator using yield
        i -= 1
for i in countdown():
    print(i)"""

"""def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))"""

"""def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word
print(list(make_word()))"""

# decorators : - are the functions that modify other functions
def decor(func):
    def wrap():
        print("=====")
        func()
        print("=====")
    return wrap
def print_text():
    print("Hello world!")
decorated = decor(print_text)
decorated()
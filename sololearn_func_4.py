# sets
"""num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print(3 in num_set)
print("spam" not in num_set)"""

"""nums = {1,2,1,3,1,4,5,6}
print(nums)
nums.add(-7)    # in sets instead of append add is used
nums.remove(3)
print(nums)"""

"""first = {1,2,3,4,5,6}
second = {4,5,6,7,8,9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)"""

# iterpools
from iterpools import count
"""for i in count(3):
    print(i)
    if i >= 11:
        break"""

a={1, 2}
print(len(list(product(range(3), a))))
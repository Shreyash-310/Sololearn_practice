# 1
"""nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))

a = (lambda x: x*(x+1))(6)
print(a)"""
# Each number in the sequence is the sum of the two numbers that precede it.
num = int(input())
Nums = list(range(num))


def fibonacci(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    else:
        return fibonacci(x - 2) + fibonacci(x - 1)


L = list(map(fibonacci, Nums))
for i in L:
    print(i)

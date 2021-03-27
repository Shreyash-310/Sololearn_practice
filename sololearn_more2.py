"""# string formatting
nums = [4,5,6]
msg = "Numbers {0} {1} {2}".format(nums[0],nums[1],nums[2])
print(msg)
print("{0}{1}{0}".format("abra","cad"))"""
"""print(",".join(["spam","eggs","ham"]))
print("spam,eggs,ham".split(","))

a = min([sum([11, 22]), max(abs(-30), 2)])
print(a)"""

"""nums = [55,44,33,22,11]
if all([i>5 for i in nums]):
    print("All are greater than 5")
if any([i%2==0 for i in nums]):
    print("At least one is even")
for v in enumerate(nums):
    print(v)"""

"""filename = input("Enter a filename: ")

with open(filename) as f:
   text = f.read()

print(text)"""

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
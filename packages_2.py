"""for i in range(10):
   if i > 5:
      print(i)
      break
else:
   print("7")"""

"""try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)"""


"""def function():
    print("This is a module function")

if __name__ == "__main__":
    print("This is a script")"""

"""import packages
packages.function()"""

"""def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)"""

for i in range(10):
  try:
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)
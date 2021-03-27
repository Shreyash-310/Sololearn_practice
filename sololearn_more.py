"""foo = print()
if foo == None:
   print(1)
else:
   print(2)"""

"""primes = {1:2,2:3,4:7,7:17}
print(primes[primes[4]])"""

"""pairs = {1:"apple","orange":[2,3,4],True:False,None:True}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))"""

"""fib = {1:1,2:1,3:2,4:3}
print(fib.get(4,0))
print(fib.get(7,5))
print(fib.get(4,0)+fib.get(7,5))"""

"""sqs = [0,1,4,9,16,25,36,49,81]
print(sqs[7:5:-1])"""
# list comprehensions
a = [x * 10 for x in range(5, 9)]
print(a)

"""strg = input()
List1 = []
List1[:0]=strg
print(List1)
print(any[char.isalnum() for char in List1])
print(any[char.isalpha() for char in List1])
print(any[char.isdigit() for char in List1])
print(any[char.islower() for char in List1])
print(any[char.isupper() for char in List1])"""

S = input()
print(any(char.isalnum() for char in S))
print(any(char.isalpha() for char in S))
print(any(char.isdigit() for char in S))
print(any(char.islower() for char in S))
print(any(char.isupper() for char in S))
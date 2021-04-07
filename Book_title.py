"""s = 'Harry Potter'
s = 'Another book'
s = list(s)
z = len(s)
Z = str(z)
code = s[0] + Z
print(code)"""

file = open("books.txt", "r")
for line in file:
    if line[-1] == "\n":
        print(line[0] + str(len(line) - 1))
    else:
        print(line[0] + str(len(line)))
file.close()

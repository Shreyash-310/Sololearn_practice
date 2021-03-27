myfile = open("filename.txt")   # to open the file named filename.txt
# open function is used to access files
# r menas read
# w means write
# a means append
# rb binary read mode
# textfile.close()  -- used to close file

#readding files
"""
file = open("filename.txt")
cont = file.read()
print(cont)
file.close()"""

# we can read the file once, another attempt to read will return empty string
# read number of lines
"""x = len(open("filename.txt").readlines())
print(x)"""

# writing files
"""file = open("filename.txt","w")
file.write("This is generated from prg.")
file.close()
file = open("filename.txt","r")
print(file.read())
file.close()"""

# working with files
"""try:
    f = open("filename.txt")
    print(f.read())
finally:
    f.close()"""

with open("filename.txt") as f:
    print(f.read())
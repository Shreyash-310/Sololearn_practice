"""file = open("filename.txt","r")
print(file.read())

file = open("filename.txt","w")
file.write("A \nB")
#file.write("A12")
file.close()
file = open("filename.txt","r")
print(file.read())
file.close()"""
with open("filename.txt", "a") as f:
    f.write("new line\n")
with open("filename.txt", "r+") as f:
    old = f.read()  # read everything in the file
    f.seek(0)  # rewind
    f.write("new line\n" + old)  # write the new line before
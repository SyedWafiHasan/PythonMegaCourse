# file = open("file.txt", 'r')
# content = file.read()
# print(content)
# file.seek(0)
# content = file.readlines()
# print(content)
# content = [i.rstrip("\n") for i in content]
# print(content)
# file.close()

file = open("file1.txt", 'w')
file.write("Line 2")
file.close()
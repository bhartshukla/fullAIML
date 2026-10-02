# --> open
# --> OPeration (CRUD)


# file operation 
# Open , read , close 
# r - read mode 
# w - write mode

# f = open("textfile.txt",r)

# f = open("demo.txt", "r") # file object return
f = open("demo.txt", "w") # file object return

# data  =f.read()
# print(type(data))
# print(data)

# f.colse() # always close file ...

# data2 = f.readline() 
# print(data2)

# data2 = f.readline() 
# print(data2)

f.write("text to override by new data ")

f.close() # always close file ...
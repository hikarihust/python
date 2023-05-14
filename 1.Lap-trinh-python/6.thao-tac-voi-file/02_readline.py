# readline
# fileObj  = open("data.txt", mode = "r")
# line1    = fileObj.readline()
# line2    = fileObj.readline()
# line3    = fileObj.readline()
# line4    = fileObj.readline()
# print(line1)
# print(line2)
# print(line3)
# print(line4)
# fileObj.close() 

# readlines
# fileObj  = open("data.txt", mode = "r")
# data    = fileObj.readlines()
# print(type(data))
# print(data)
# fileObj.close() 

# list
fileObj  = open("data.txt", mode = "r")
data     = list(fileObj)
print(data)
fileObj.close() 

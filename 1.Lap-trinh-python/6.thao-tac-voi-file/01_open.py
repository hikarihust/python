# python file
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

fileObj = open("data.txt", mode = "r")

# Đọc hết nội dung trong file
# data    = fileObj.read()
# print(data)
# fileObj.close() 

# Đọc từng ký tự trong file
# data1    = fileObj.read(1)
# data2    = fileObj.read(2)
# print(data1)
# print(data2)
# fileObj.close() 

# Con trỏ trong file
data1    = fileObj.read(1)
fileObj.seek(0)
data2    = fileObj.read(1)
print(data1)
print(data2)
fileObj.close() 

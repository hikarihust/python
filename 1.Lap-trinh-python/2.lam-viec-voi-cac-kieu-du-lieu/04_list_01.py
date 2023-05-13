myList = ["a", "b", "c"]
myList = [1, 2, 3]
myList = [1, 2, 3, "a", "b", "c", ["d", "e"]]

# Kiểm tra sự tồn tại
print("a" in myList)
print("aA" not in myList)

# Index
myList = [1, 2, 3, "a", "b", "c", ["d", "e"]]
print(myList[0])
print(myList[-1])
print(myList[6][1])

# Trích xuất
myList = ["a", "b", "c"]
print(myList[2:])
print(myList[0:2])

# Cập nhật phần tử
myList = ["a", "b", "c"]
myList[0] = "Tada"
print(myList)

# Xóa phần tử
myList = ["a", "b", "c"]
del myList[0]
print(myList)

# append
myList = ["a", "b", "c"]
myList.append("Python")
print(myList)

myList = ["a", "b", "c"]
myList.append(["x", "y"])
print(myList)

myList = ["a", "b", "c"]
myList.extend(["x", "y"])
print(myList)
#pop
myList = ["a", "b", "c"]
item = myList.pop(1)
print(item)
print(myList)
# Input     : Cho 1 list chứa các chuỗi
# Output    : Phần tử có chiều dài lớn nhất
# Ví dụ     : ["PHP", "Exercises", "Backend"] phần tử có chiều dài lớn nhất: Exercises

myList = ["PHP", "Exercises", "Backend"]

result  = ""
count   = 0
# for elm in myList:
#     if len(elm) > count:
#         count = len(elm)
#         result= elm

# print(result)

result = max(myList, key = len)
print(result)
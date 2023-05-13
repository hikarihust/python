myStr = "hello"
myStr = 'python'
myStr = "I'm Python"

str1 = "hello"
str2 = "python"

# Nối chuỗi
result1 = str1 + "----" + str2
print(result1)

# Nối số và chuỗi
result1 = "Result: " + str(1+2)
print(result1)

# Nhân bản chuỗi N lần
result2 = (str1 + " ") * 5
print(result2)

# Kiểm tra sự tồn tại của chuỗi
result3 = "hello" in str1 
print(result3)

# Index trong chuỗi
# "hello"

result4 = str1[3]   # Chỉ số trong chuỗi 0 1 2 3   
result5 = str1[-1]  # Lấy ký tự cuối chuỗi
result6 = str1[len(str1) - 1]  # Lấy ký tự cuối chuỗi
print(result4)
print(result5)
print(result6)

# Thay đổi giá trị của phần tử trong chuỗi: str1[0] = "d" không thể 

# Trích xuất chuỗi
myStr   = "hello python"
result7 = myStr[:]  # Cũng giốngg với result7 = myStr
print(result7)
result7 = myStr[2:] # from:to-1 -> Lấy từ chỉ số 2 cho đến cuối chuỗi
print(result7)
result7 = myStr[:2] # Lấy từ chỉ số 0 cho đến chỉ số 1
print(result7)
result7 = myStr[2:4]  # Lấy từ chỉ số 2 cho đến chỉ số 3
print(result7)
result7 = myStr[::3] # Không truyền from và to, có bước nhảy là 3 -> hlph
print(result7)
result7 = myStr[::-1]  # đảo ngược chuỗi
print(result7)
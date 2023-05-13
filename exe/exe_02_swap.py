# Input : Cho 2 chuỗi x = "abc", y = "xyz"
# Output: Tạo ra chuỗi mới xyc abz
                                        
x = "abc"
y = "xyz"

xNew = y[:len(y)-1] + x[-1]
yNew = x[:len(x)-1] + y[-1]

result = xNew + " " + yNew
print(result)

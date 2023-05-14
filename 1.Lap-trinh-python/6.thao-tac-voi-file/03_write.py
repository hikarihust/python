# https://www.tutorialspoint.com/python/python_files_io.htm
# write
# Test mode = r     reading only
# Test mode = r+    reading and writing, mặc định là từ vị trí đầu tiên, nếu vị trí đó có ký tự rồi thì thực hiện ghi đè
# Test mode = w     writing only  ----- Ghi đè
# Test mode = a     appending     ----- Ghi vào cuối
fileObj  = open("data.txt", mode = "a")
fileObj.write("\nLine")
fileObj.close()
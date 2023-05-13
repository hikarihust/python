# Input     : Nhập vào tên tập tin
# Output    : In ra phần mở rộng của tập tin

fileName    = input("Nhập vào tên tập tin: ")

fileExt     = fileName.split(".")
tmp         = len(fileExt)

result      = "Không xác định"
if(tmp > 1):
      result = fileExt[tmp - 1]

print("Phần mở rộng của tập tin: " + result)

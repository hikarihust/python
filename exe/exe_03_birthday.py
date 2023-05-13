# Input : Nhập vào tên và năm sinh
# Output: Xin chào [name], năm nay bạn [age] tuổi

# python get current year
# https://stackoverflow.com/questions/28189442/datetime-current-year-and-month-python/28189525


# - năm hiện tại
# - lấy giá trị mà người dùng họ nhập vào

from datetime import datetime

currentYear = datetime.now().year

name        = input("Nhập vào tên của bạn: ")
birthday    = int(input("Nhập vào năm sinh của bạn: "))
result      = "Xin chào {name}, năm nay bạn {age} tuổi".format(name=name, age = currentYear - birthday)
print(result)

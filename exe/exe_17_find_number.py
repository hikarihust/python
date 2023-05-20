# Input     : Lấy các giá trị số trong một chuỗi và đưa vào 1 list
# Output    : [1,2,10]
# Ví dụ     : Exercises number 1, 12, 13, and 345 are important
# Ví dụ     : [1, 12, 13, 345]

import re
text    = "Exercises number 19, 12, 13, and 345 are important"

listResult = []
for n in re.finditer("[0-9]{1,}", text):
    listResult.append(int(n.group()) )

print(listResult)
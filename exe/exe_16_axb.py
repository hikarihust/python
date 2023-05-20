# Input     : Kiểm tra mẫu chuỗi bất kỳ có thỏa mãn: Bắt đầu bằng a và kết thúc bằng b
# Output    : Match hoặc Not match
# python regular expression match vs search

import re
def checkAxB(text):
    patterns = '^a.*b$'
    if re.match(patterns,  text):
        return 'Match!'
    else:
        return('Not match!')

print(checkAxB("ab"))
print(checkAxB("1ab"))
print(checkAxB("ab1"))
print(checkAxB("1ab1"))
print(checkAxB("adsdsdasda1231321b"))

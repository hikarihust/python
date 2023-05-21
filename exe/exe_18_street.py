# Input     : Chuỗi địa chỉ kết thúc với từ street
# Output    : thay từ street thành st.
# Ví dụ     : 21 To Hien Thanh street
# Ví dụ     : 21 To Hien Thanh sTREet
# Ví dụ     : 21 To Hien Thanh st.
#

import re
inputText = '21 To Hien Thanh street'
result  = re.sub('street$', 'st.', inputText, flags= re.I) # flags=re.I
print(result)

inputText = '21 To Hien Thanh strEet'
result  = re.sub('street$', 'st.', inputText, flags= re.I) # flags=re.I
print(result)

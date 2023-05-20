import re 

pattern = "\\D"
text    = "0383-308-983 Mr Quang"

result = re.sub(pattern, "", text)
print(result)
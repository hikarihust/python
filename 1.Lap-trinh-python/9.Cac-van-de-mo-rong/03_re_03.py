# https://www.youtube.com/results?search_query=zendvn+regular+experssion
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
import re 

pattern = "abc"
pattern = ".*abc"
text    = "123 abc xabc 456"
match = re.search(pattern, text)

if re.search(pattern, text):
     print (match.group())
else :
    print("Not Found")

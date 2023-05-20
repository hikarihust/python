# https://www.youtube.com/results?search_query=zendvn+regular+experssion
# https://www.tutorialspoint.com/python/python_reg_expressions.htm
import re 

pattern = ".*abc.*"
text    = "123 abc xabc 456"

match = re.match(pattern, text)
if match:
    print("Found")
    print(match)
else :
    print("Not Found") 

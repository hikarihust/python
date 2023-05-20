import re 

pattern = "[a-z]{3}-[1-9]{2}"  
text    = "auc-39"

match = re.match(pattern, text)
if match:
    print("Found")
else :
    print("Not Found")

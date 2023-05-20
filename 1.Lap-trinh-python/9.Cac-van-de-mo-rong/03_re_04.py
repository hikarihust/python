
import re 

pattern = "[A-Z]{3}-[1-9]{2}"
text    = "adc-12"

match = re.match(pattern, text, re.IGNORECASE)
if match:
    print("Found")
else :
    print("Not Found")
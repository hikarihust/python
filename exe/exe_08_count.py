# Input     : google.com
# Output    : {'g':2, 'o':3, 'l':1, 'e': 1, '.': 1, 'c':1, 'm':1}

myString = 'google.com'
result   = {}
for n in myString:
    keys = result.keys()
    if n in keys:
        result[n] += 1
    else:
        result[n] = 1
   
for elm in result:
    print(elm, ": ", result[elm])
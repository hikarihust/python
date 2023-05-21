import json

import functions as myFuncs


json_data   =   open("data.json").read()

data        = json.loads(json_data)
keyword     = input("Keyword: ")
result      = myFuncs.findWord(keyword, data)
print(result)

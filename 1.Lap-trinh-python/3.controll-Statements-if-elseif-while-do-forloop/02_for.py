# myList = ["node", "python", "abc"]

# for item in myList:
#     if(item == "node"):
#         print(item)
#     else:
#         print("Khóa học: " + item)
    

myDic = {'name': 'quangvu', 'age': 18, 'score': [7,8,9]}

for key in myDic:
    if(key == "score"):
        print("Key: %s - Value: %d" %(key, sum(myDic[key])) ) 
    else:
        print("Key: %s - Value: %s" %(key, myDic[key]))

myDic = {'name': 'quangvu', 'age': 18}
print(myDic)
print(myDic['name'])
myDic = {'name': 'quangvu', 'age': 18, 'score': [7,8,9]}
print(myDic)
print(myDic['score'][2])

myDic['name'] = "vudinhquang"
print(myDic)

myDic['address'] =  {}
myDic['address']['city']        =  "ho chi minh"
myDic['address']['district']    =  "quan 9"
print(myDic)

del myDic['address']['district'] 
print(myDic)
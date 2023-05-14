import json

fileOne     = "data/info.txt"
fileTwo     = "data/score.txt"
fileStudent = "data/student.txt"

data    = []
with open(fileOne) as fileInfo, open(fileTwo) as fileScore:
    for lineInfo, lineScore in zip(fileInfo,fileScore):
        data.append({
            'name': lineInfo.rstrip(),
            'score': lineScore.rstrip()
        })

with open(fileStudent, 'w') as fileStudentObj:
    fileStudentObj.write(json.dumps(data)) 

data = ""
with open(fileStudent, 'r') as fileStudentObj:
    data = fileStudentObj.read()

print(data)
print(type(data))
result = json.loads(data)
print(result)
print(type(result))

for info in result:
    print ("- Name: {}\n- Score: {}".format(
        info["name"],
        info["score"]
    ))
    print("-------------------------")
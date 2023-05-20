class Student():
    school = "hust"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("Name: {name} - Age: {age}".format(name = self.name, age = self.age))

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

x  = Student(name="quangvu", age=18)
x.showInfo()
print(x.getAge())
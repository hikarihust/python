class Student():
    school = "hust"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        print("Name: {name} - Age: {age}".format(name = self.name, age = self.age))

    def showInfoHello(self):
        print("Hello")

x  = Student(name="quangvu", age=18)
x.showInfo()
x.showInfoHello()
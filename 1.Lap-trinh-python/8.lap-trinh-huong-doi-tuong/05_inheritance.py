class People():
    
    def __init__(self, name, age):
        print("People __init__" )
        self.name = name
        self.age = age

    def showInfo(self):
        print("Name: {name} - Age: {age}".format(name = self.name, age = self.age))

    def setAge(self, age):
        self.age = age

class Student(People):
    
    def __init__(self, name, age, school):
        People.__init__(self, name, age)
        self.school = school
        print("Student __init__" )

    def showInfo(self):
        People.showInfo(self)
        print("school: {school}".format(school = self.school))

    def setSchool(self, school):
        self.school = school

x  = Student(name="quang", age=18, school="hust")
x.showInfo()
x.setSchool("hust.com")
x.showInfo()
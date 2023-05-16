class Student():
    school = "hust"
    def __init__(self, paramName, paramAge):
        self.name   = paramName
        self.age    = paramAge

x  = Student(paramName="quangvu", paramAge=18)
print(x.age)
print(x.name)
print(x.school)

y  = Student("haiyen", 1)

print(y.age)
print(y.name)
print(y.school)
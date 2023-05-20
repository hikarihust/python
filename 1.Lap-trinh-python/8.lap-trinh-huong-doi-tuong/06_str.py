class Student():
    

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __str__(self):
        return  "Name: {name} - Age: {age}".format(name = self.name, age = self.age)

x  = Student(name="quangvu", age=18)
y  = Student(name="haiyen", age=1)
print(x)    # in đối tượng __str__
print(y)    # in đối tượng __str__

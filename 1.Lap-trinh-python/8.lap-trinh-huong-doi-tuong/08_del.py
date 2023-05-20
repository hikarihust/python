class Student():
    

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):    
        return  "Name: {name} - Age: {age}".format(name = self.name, age = self.age)
    
    def __del__(self):
        print("success")

x  = Student(name="quangvu", age=18)
print(x)
del x
try:
    print(x)
except NameError:
    print ("This object is deleted")

class Student():
    

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def __len__(self):
        return len(self.name)

x  = Student(name="quangvu", age=18)
y  = Student(name="haiyen", age=1)
print(len(x))    
print(len(y))    

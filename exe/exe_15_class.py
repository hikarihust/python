class Course():
    
    def __init__(self, name, time, price):
        self.name = name
        self.time = time
        self.price = price

    def showInfo(self):
        print("Name: {name} - time: {time} - price: {price}".format(
            name    = self.name, 
            time    = self.time,
            price   = self.price
        ))

    def __str__(self):
        return  "Name: {name} - time: {time} - price: {price}".format(
            name    = self.name, 
            time    = self.time,
            price   = self.price
        )

listCourses = [
    {'name': 'PHP', 'time': 12, 'price': 20},
    {'name': 'Django', 'time': 24, 'price': 40}

]

print(listCourses)

result = []
for course in listCourses:
    result.append(Course(course["name"],course["time"],course["price"]))


for courseObj in result:
    print(courseObj)

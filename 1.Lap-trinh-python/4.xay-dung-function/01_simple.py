def showHello():
    print("Xin chào Nguyễn Văn A")

def showInfo2(name = "quangvu", age = 18):
    if name is None:
        name = "quangvu"
    print( "Name: {}, age: {}".format(name, age) )

showHello()
showInfo2()
showInfo2("tada")
showInfo2(None, 99)
showInfo2("quangvu", 199)
showInfo2(age = 120, name = "quangvu")
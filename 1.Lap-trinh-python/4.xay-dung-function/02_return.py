def showResult(num1, num2):
    return "{num1} + {num2} = {total}".format(
        num1 = num1,
        num2 = num2,
        total = addNum(num1, num2)
    )

def addNum(num1, num2): 
    return num1 + num2

x = 5
y = 20
print(showResult(x,y))
if(addNum(x,y) > 10):
    print("BIG")
else:
    print("SMALL")

x = 25

def myFunc():
    global x
    x = 50 
    print(x)
    return x

print(x)            
print(myFunc())     

myFunc()
print("After: ",x)            
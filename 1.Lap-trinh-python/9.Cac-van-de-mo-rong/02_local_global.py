x = 25

def myFunc():
    y = 100
    print(locals())
    print("------------------")
    print(globals())
    print("------------------")
    print(locals()["y"])
    print("==================")
    print(__file__)


myFunc()
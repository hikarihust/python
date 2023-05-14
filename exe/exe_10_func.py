# Input     : Cho 1 list chứa các khóa học
# Output    : In ra thông tin khóa học
# ---------Info - Start---------
# -Name: PHP
# -Type: Free
# ==========Info - End==========

myList = [
    {'name': 'PHP', 'free': True},
    {'name': 'Python', 'free': False}
]

def showCourseType(type):
    if(type == True):
        return "Free"
    else:
        return "No Free"

def showOutline(content, character = "-", newLine = False):
    if (newLine == True): print (content.center(30, character), '\n')
    else: print (content.center(30, character))

def showCourseInfo(course):
    print("-Name: {name} \n-Type: {type}".format(
        name    = course['name'],
        type    = showCourseType(course['free']),
    ))

def showList(myList):
    for course in myList:
        showOutline("Info - Start")
        showCourseInfo(course)
        showOutline("Info - End", "=", True)

showList(myList)
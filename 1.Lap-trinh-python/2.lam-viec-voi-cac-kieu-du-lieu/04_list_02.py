myList = ["a", "b", "c"]

#reverse
myList.reverse()
print(myList)

#sort
myList = [1,4,2,9,12,7]
myList.sort()               #asc
print(myList)
myList.sort(reverse=True)   #desc
print(myList)

#count
myList = ["a", "a", "b", "c"]
print(len(myList))
print(myList.count("a"))

#clear
myList = ["a", "a", "b", "c"]
myList.clear()
print(myList)
print(len(myList))
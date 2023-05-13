str1 = "Python is %s !!" %('easy')
print(str1)
str2 = "Python is %s !! Python is %s !!" %('easy', 'free')
print(str2)
strTemplate = "Khóa học: %s - Học phí: %s"
strPython   = strTemplate %('python', '10$')
strPHP      = strTemplate %('php', 'free')
print(strPython)
print(strPHP)

result1 = "Item one: {}".format("a")
print(result1)
result1 = "Item one: {} Item two: {}".format("a","b")
print(result1)
result1 = "Item one: {x} Item two: {y}".format(x="a", y = "b")
print(result1)
result1 = "Item one: {y} Item two: {x}".format(x="a", y = "b")
print(result1)

x = "A"
y = "B"
result2 = f'Item one: {x} Item two: {y}'

print(result2)
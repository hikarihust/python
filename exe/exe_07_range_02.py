# Input     : [a,b] và n (ví dụ n = 3)
# Output    : In ra list [a1, b1, a2, b2, a3, b3]

myList = ['a', 'b']
n = 4

result = ["{}-{}".format(elm, index) for index in range(1, n+1) for elm in myList ]
print(result)
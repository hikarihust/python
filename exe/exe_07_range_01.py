# Input     : [a,b] và n (ví dụ n = 3)
# Output    : In ra list [a1, b1, a2, b2, a3, b3]

myList = ['x', 'y', 'z']
n = 2

result = []
for item in myList:
	for index in range(1, n + 1):
		elm = "{}-{}".format(item, index)
		result.append(elm)

print(result)

from collections import Counter

dictOne = {'a': 100, 'b': 100, 'c':300}
dictTwo = {'a': 300, 'b': 200, 'd':400, 'c':400}

result  = dict(Counter(dictOne)+Counter(dictTwo))

print(result) 
    
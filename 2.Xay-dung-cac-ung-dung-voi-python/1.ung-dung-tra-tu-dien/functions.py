from difflib import get_close_matches

def findWord(keyword, data):
    result = "Not found"
    if keyword in data:
        result = showWord(data[keyword])
    else:
        result = "Not found"
    
    return result
    
def showWord(word):
    spelling = word[0]
    means    = join(word[1:], "\n")

    return "Spelling: {spelling} \nMeans:\n{means}".format(
        spelling    = spelling, 
        means       = means 
    )

def join(listInput, sep):
    result = ''
    for el in listInput:
        result += '+ {}{}'.format(el, sep)
    return result
    
from difflib import get_close_matches

def findWord(keyword, data):
    result = "Not found"
    if keyword in data:
        result = showWord(data[keyword])
    else:
        result = "Not found"
    
    return result
    
def showWord(word):
    print('showWord')
    return word

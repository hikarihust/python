from difflib import get_close_matches

def findWord(keyword, data):
    result = "Not found"
    if keyword in data:
        result = showWord(data[keyword])
    else:
        listSuggest = get_close_matches(keyword, data.keys(), 3)
        if(len(listSuggest) > 0) :
            for suggest in listSuggest:
                confirm = input("Bạn muốn tìm từ: {} (Enter y if yes, or n if no): ".format(suggest) )
                if (confirm == "y"):
                    result = showWord(data[suggest])
                    break
                elif (confirm == "n"):
                    continue
                else :
                    result = "No valid"
                    break
    
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
    
# https://kite.com/python/docs/difflib.get_close_matches

from difflib import get_close_matches

myStr     = "appel"
myList    = ['ape', 'apple', 'app','peach', 'puppy']

result    = get_close_matches(myStr, myList, 1)
print(result)
    
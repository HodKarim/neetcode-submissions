from typing import List

'''

take list of strings (words)
returns True if there are any duplicate strings, false if otherwise

convert list into set
compare length of list to created set

works because sets have no duplicates (all unique)
'''

def contains_duplicate(words: List[str]) -> bool:
    new_set = set(words)

    if len(new_set) == len(words):
        return False
    else: 
        return True

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))

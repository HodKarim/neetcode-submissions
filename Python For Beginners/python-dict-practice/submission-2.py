from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    dictt = {}
    for i in range(len(word)):
        if word[i] in dictt:
            dictt[word[i]] +=1
        else:
            dictt[word[i]] = 1
    return dictt

'''
take string word and return dictionary with count of each character in word

word[i]
'''


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

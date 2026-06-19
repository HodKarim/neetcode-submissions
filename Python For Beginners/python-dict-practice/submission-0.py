from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    '''
    implementing a function that takes a string word
    returns a dictionary with count of each character in the word
    key = char
    value = count

    for loop that traverses through each element and adds them to the 
    dictionary. it should first check if it exists. if it doesnt exist, 
    add it. if it does exist, increment the value

    
    '''

    dictt = {}

    for char in word:
        if char in dictt:
            #increment value
            value = dictt[char] + 1
            dictt[char] = value
            
        else:
            # add to dictionary
            dictt[char] = 1
    return dictt





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))

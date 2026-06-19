from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    dict1 = {} #create new dictionary
    dict1[name] = age
    return dict1

def list_to_dict(words: List[str]) -> Dict[str, int]:
    #take list of strings (words)
    #map each string to its index in the list
    #return resulting dict

    dict2 = {}

    i = 0
    for i in range(len(words)):
        #take word in words and map to its index in list
        dict2[words[i]] = i

    return dict2



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))

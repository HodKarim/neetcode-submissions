from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    #create a dict, map name to age then return the dict

    new_dict = {}
    new_dict[name] = age

    return new_dict


def list_to_dict(words: List[str]) -> Dict[str, int]:
    #take a list of strings (words) and map each string to its index then return
    #resulting dict

    dictt = {}
    for i in words:
        dictt[i] = words.index(i)

    return dictt



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))

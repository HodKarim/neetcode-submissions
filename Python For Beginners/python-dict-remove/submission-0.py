from typing import Dict, List

def remove_keys(my_dict: Dict[str, int], keys: List[str]) -> Dict[str, int]:
    for i in keys:
        if i in my_dict:
            my_dict.pop(i)
        else:
            continue
    return my_dict
'''
parameters: dictionary my_dict, list of strings keys
goal: remove all keys in list from the dictionary and return modified dict
    if key not there, ignore

for loop that loops through all the elements in list keys
    if  key exists inside dictionary
        delete key
    else:
        continue
return dictionary

'''





# do not modify below this line
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["a", "c"]))
print(remove_keys({"a": 1, "b": 2, "c": 3}, ["d"]))

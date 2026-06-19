from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    new_list = []
    for key, value in age_dict.items():
        # add them into a list
        new_list.append(key)
    return new_list
        

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    other_list = []
    for key, value in age_dict.items():
        # add them into a list
        other_list.append(value)
    return other_list

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))

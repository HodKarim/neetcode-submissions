from typing import Dict, List

'''
accept dictionary of names and ages and returns list of all ages (values)
'''

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    values = list(age_dict.values())

    return values
    

# do not modify below this line
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35}))
print(get_dict_values({"Alice": 25, "Bob": 30, "Charlie": 35, "David": 40}))

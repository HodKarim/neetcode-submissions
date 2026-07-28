from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    '''
    takes 2 lists, keys and values, and returns hashmap where keys are elems of
    keys and values are elems of values
    '''
    hashmapp = {}
    for key, value in zip(keys, values):
        hashmapp[key] = value
    return hashmapp



def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    '''
    takes hashmap and list of keys and returns list of values associated w those keys
    '''
    values = []
    for key in keys:
        values.append(hash_map[key])
    return values


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))

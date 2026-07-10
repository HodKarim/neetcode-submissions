from typing import List


def is_arr_valid(names: List[str], max_length: int) -> bool:
    #function that returns true if length of names list is greater than 0 and less than or equal to max_length
    if 0 < len(names) <= max_length:
        return True
    else:
        return False



# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))

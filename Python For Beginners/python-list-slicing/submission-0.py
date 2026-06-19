from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    #return list containing last three elements of my_list

    new_list = [my_list[-3], my_list[-2], my_list[-1]]
    return new_list


# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))

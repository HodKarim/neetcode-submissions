from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    #remove the element at a given index (int)
    my_list.pop(index)
    return my_list


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    for i in range(0,n):
        my_list.pop()
    return my_list
    #pop the lst n elements from my list and return modified list

#were going to keep doing my_list.pop() until we reach n times so from 0 to n?





# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))

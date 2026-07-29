from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    '''
    tskes list and returns new list of ints in reverse order
    stack is lifo, last in is first out
    take list pop each elem and add to new list
    '''
    listt = list()
    for i in range(len(arr)):
        listt.append(arr.pop())
    return listt


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

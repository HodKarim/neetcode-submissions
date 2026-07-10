from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    arr1 = list(arr)
    arr1.remove(element)
    return arr1
'''
given: list arr, int element, return list
goal: implement function that takes a list of ints & returns [new list] with element removed
constraint: assume always in list

'''



# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)

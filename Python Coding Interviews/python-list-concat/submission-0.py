from typing import List


def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    #given: arr1, arr2, both arrays
    #goal: take 2 lists and return new list with all elements of first list first and then second list
    result = arr1 + arr2
    return result


# do not modify below this line
arr1 = [1, 3, 5]
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)

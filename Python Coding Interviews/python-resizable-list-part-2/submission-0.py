from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1

#given: arr2 and arr2
#goal: append the elements of arr2 to end of arr1 & return result
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for i in range(len(arr2)):
        if arr2[i] in arr1:
            arr1.remove(arr2[i])
    return arr1

#given: arr1, arr2, return list
#goal: remove all elements of arr2 from arr1 and return 


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))

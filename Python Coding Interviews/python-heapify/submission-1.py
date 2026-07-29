import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    '''
    takes list of strings and returns list into min heap
    '''
    heapq.heapify(strings)
    return strings


def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)
    return integers


def heap_sort(nums: List[int]) -> List[int]:
    '''
    takes list of integers and returns list of integers
    sorted in ascending order (1,2,3)
    '''
    heapq.heapify(nums)
    listt = []
    for i in range(len(nums)):
        listt.append(heapq.heappop(nums))
    return listt


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))

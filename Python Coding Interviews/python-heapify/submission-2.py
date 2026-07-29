import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    '''
    takes list of strings and returns list transformed into min heap
    '''
    heapq.heapify(strings)
    return strings


def heapify_integers(integers: List[int]) -> List[int]:
    '''
    same but for ints
    '''
    heapq.heapify(integers)
    return integers


def heap_sort(nums: List[int]) -> List[int]:
    '''
    takes list of ints and returns list sorted in ascending order
    so we get a minheap, pop each elem and add to a list
    '''  
    listt = []
    heapq.heapify(nums)
    for i in range(len(nums)):
        listt.append(heapq.heappop(nums))
    return listt



# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))

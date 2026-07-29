import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    '''
    takes list of ints and returns ints in reverse sorted order

    push elements into list and turn element back into positive at same time
    '''
    
    for i in range(len(nums)):
        nums[i] *= -1
    heapq.heapify(nums)

    result = []

    while nums:
        result.append(-heapq.heappop(nums))
    return result






# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

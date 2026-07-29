import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    '''
    max heap using pairs. make first pair the negative number
    '''
    
    for i in range(len(nums)):
        nums[i] = (nums[i] * -1, nums[i])
        

    heapq.heapify(nums)
    result = []

    while nums:
        pair = heapq.heappop(nums)
        result.append(pair[1])
    return result



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))

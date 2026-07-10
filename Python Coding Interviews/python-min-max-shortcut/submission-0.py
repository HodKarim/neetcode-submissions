from typing import List


def disallow_negatives(num: int) -> int:
    #takes integer and returns int if greater than or equal to 0, otherwise return 0
    return max(num, 0)


def max_difference(nums: List[int]) -> int:
    #takes list of ints andreturns maximim difference between any 2 adjacent elements
    #thru subtracting element on right from element on left
    maxx = 0
    for i in range(len(nums)):
        if i == 0:
            continue
        else:
            maxx = max(maxx, nums[i] - nums[i-1])
    return maxx

    '''
    [1,3,5,7,10]

    maxx = 0
    0 vs 3-1 = 2
    maxx = 2

    2 vs 5-3 = 2
    .. vs 
    '''



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))

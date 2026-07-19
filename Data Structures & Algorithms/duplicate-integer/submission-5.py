class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_set = set(nums)

        if len(new_set) == len(nums):
            return False
        else:
            return True

'''
given: integer array nums
goal: return true if any value appears more than once, otherwise false

solution:
array to a set.
len array to len of set

O(1)
'''


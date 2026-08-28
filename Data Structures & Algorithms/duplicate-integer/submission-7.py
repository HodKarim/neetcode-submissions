class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        nums_set = set(nums)

        if len(nums) == len(nums_set):
            return False
        else:
            return True
'''
given: int array nums

goal: return true if value is in there more than once


use set to check for duplicates


'''
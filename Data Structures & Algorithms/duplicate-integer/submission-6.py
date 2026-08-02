class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sett = set(nums)

        if len(sett) == len(nums):
            return False
        else:
            return True

'''
given array nums
return T if value is in there more than once

sets in python do NOT allow duplicates. convert the array into a set and compare their lengths
if same, no duplicates. else, theres a duplicate


'''
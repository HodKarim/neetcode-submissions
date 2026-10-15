class Solution:
    def hasDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums_set) == len(nums):
            return False
        else:
            return True

'''
see if theres a duplicate

given integer array return true if theres dupliate


'''
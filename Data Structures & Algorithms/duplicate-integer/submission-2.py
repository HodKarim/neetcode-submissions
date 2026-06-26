class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #given int array nums
        #return True if any num appears more than once, otherwise false

        # nums = [1,2,3,3]
        '''
        given list, convert list to set and then see if the length of 
        list and set are same

        if equal, no duplicates (FALSE)
        otherwise, duplicate exists (TRUE)
        '''
        new_set = set(nums)

        if len(new_set) == len(nums):
            return False
        else:
            return True
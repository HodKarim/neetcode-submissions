class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        for num in nums: #nums MUST be equal to count
            if num != count:
                return num - 1
            count+=1
        return nums[len(nums)-1] + 1
        '''
        given an array nums with n integers in range [0,n] w no dups, 
        goal: return the number thats missing




        '''
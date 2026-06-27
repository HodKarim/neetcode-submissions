class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        anss = nums.copy()
        ans = nums + anss

        return ans


'''
given: integer array nums (length n)
goal: make array ans of length 2n where u duplicate the array

for loop but the range is n * 2

[1,4,1,2]

[1,4,1,2,1,4,1,2]

brute force:

        n = len(nums)
        ans = []
        count = 0
        for i in range(len(nums)*2):
            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[count])
                count+=1
        return ans
'''
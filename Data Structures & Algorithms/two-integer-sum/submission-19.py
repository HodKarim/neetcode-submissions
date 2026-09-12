class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]
'''
given array of ints and integer target, return indices i and j st 
nums[i] + nums[j] == target

nums = [3,4,5,6], target = 7

so double 4 loop looking for the answer

[3,4,5,6]
i
  j



'''
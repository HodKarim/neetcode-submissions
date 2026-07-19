class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[i] + nums[j] == target and i != j):
                    return [min(i,j), max(i,j)]

'''
given: array of integers (nums), integer (target)
goal: return indices i and j s.t the elements at those indices add up to target.
constraints: assume every input has exactly 1 pair of indices i and j, return answer w smaller index first

Solution:

nums = [3,4,5,6], target = 7
        i   j

for i in range(len(nums)):
    for j in range(len(nums)):
        if(nums[i] + nums[j] == target AND i != j):
            return [min(i,j), max(i,j)]


return [min(_,_), max(_,_)]
'''
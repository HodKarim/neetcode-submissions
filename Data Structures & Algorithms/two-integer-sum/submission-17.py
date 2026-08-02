class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]
'''
given array of ints nums and int target
goal is return indices i and j st nums[i] + nums[j] == target and i != j

naive approach (O(n^2)): nested for loop checking each

[3,4,5,6]
  i  j
3+4 = 7
3+5 = 8
3+6 = 9
4+5...


constraint: i and j cannot be equal or else we can get thr wrong answer (3 + 3 = 6)


'''
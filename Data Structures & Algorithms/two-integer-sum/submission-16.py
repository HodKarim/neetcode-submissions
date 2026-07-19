class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashh = {}
        for i in range(len(nums)):
            answer = target - nums[i]
            hashh[answer] = i

        for i in range(len(nums)):
            if nums[i] in hashh and i != hashh[nums[i]]:
                return [min(i, hashh[nums[i]]), max(i, hashh[nums[i]])]

'''
given: array of integers (nums), integer (target)
goal: return indices i and j s.t the elements at those indices add up to target.
constraints: assume every input has exactly 1 pair of indices i and j, return answer w smaller index first


nums=[1,3,4,2]
target=6

6-1 = 5
6-3 = 3

Solution:
O(n^2), O(n)
nums = [3,4,5,6], target = 7
        i   j

for i in range(len(nums)):
    for j in range(len(nums)):
        if(nums[i] + nums[j] == target AND i != j):
            return [min(i,j), max(i,j)]



O(n), work with hashmap instead
nums = [3,4,5,6], target = 7

7 - 3 = 4
7 - 4 = 3
7 - 5 = 2
7 - 6 = 1

{4:3, 3:4, 2:5, 1:6}

(answer = key, whats being subtracted from target = value)

hashh = {}

for i in range(len(nums)):
    answer = target - nums[i]
    hashh[answer] = nums[i]

for i in range(len(nums)):
    if nums[i] in hashh:
        return [min(nums[i], hashh[nums[i]])]
'''
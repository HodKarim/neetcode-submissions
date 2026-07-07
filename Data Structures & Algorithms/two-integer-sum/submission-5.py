class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return[min(i,j), max(i,j)]




'''
given: array nums, integer [target]
goal: return indices i and j s.t their nums[i] + nums[j] == target and they arent equal

[3,4,5,6], target = 7
^  ^
i = 0
j = 0

continue

i = 0
j = 1


'''





























'''
problem sytatement:
given an array of integers (nums) and integer target
goal: return indices i and j s.t their indices result in target (add up to)

return w smaller indice first

solution:
brute force

3 4 5 6
i j

double for loop

3 + 4 = target? no, move on

3+ 5 = target? no, move on...

for i in range(len(nums)):
    for j in range len(nums):
        if nums[i] + nums[j] == target:
            smaller_num = min(nums[i], nums[j])
            bigger_num = max(nums[i], nums[j])
            break
'''


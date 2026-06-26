class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    smaller_num = min(i, j)
                    bigger_num = max(i, j)
                    break
        list_ans = [smaller_num, bigger_num]
        return list_ans



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


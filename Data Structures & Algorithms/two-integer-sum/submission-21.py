class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = {}

        for i in range(len(nums)):
            ans = target - nums[i]
            result[ans] = i #the index of the value that gives that

        for j in range(len(nums)):
            if nums[j] in result and j != result[nums[j]]:
                return [min(j, result[nums[j]]), max(j, result[nums[j]])]
'''

O(n) approach: hashmap

[3,4,5,6]

for each one, we subtract the target from it:

7-3 = 4
7-4 = 3

7-5 = 2
7-6 = 1

then when we store the subtracted answer in a hashmap as a key for easy lookup

then we iterate thru the list one at a time and see if its in the hashmap


'''
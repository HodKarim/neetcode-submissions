class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            # if weve alr seen the complement, thats the answer simple
            if complement in seen:
                return [seen[complement], i]

            #store current number and its index
            seen[nums[i]] = i

'''
Logic:
iterate through the array once
for each number, calculate the complement (target - current number)
check if the complement has already been seen
if yes, return the index of the complement and current index
otherwise, store the current number and its index in the hashmap

Pattern:
Hash Map / Lookup Table

Time Complexity:
O(n)
we only traverse the array once and each hashmap lookup/insertion
takes O(1) on avg because of this

Space Complexity:
O(n)
in the worst case we store every number in the hashmap

Time to complete problem:
18 minutes 31 seconds
'''
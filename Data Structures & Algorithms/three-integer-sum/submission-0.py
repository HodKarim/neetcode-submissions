class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array first!!!!!
        nums.sort()

        result = []

        for i in range(len(nums) - 2):
            #skip duplicate first nums
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    #skip duplicate second nums
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    #skip duplicate third nums
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    #need larger sum
                    left += 1

                else:
                    #need smaller sum
                    right -= 1

        return result


'''
Logic:
first, sort the array
next, fix one number at index i.
use two pointers (left and right) to find two numbers that make the total sum equal to 0
if sums too small, move left pointer right
if sums too large, move right pointer left
if sums 0, save the triplet and skip duplicates. repeat for every possible first num

Pattern:
Two Pointers + Sorting (mainly just two pointer imo)

Time Complexity:
O(n^2)
Sorting takes O(n log n), and the two-pointer scan runs O(n)
for each element, resulting in O(n^2) overall.

Space Complexity:
# O(1) extra space (ignoring output list)

Time to complete problem: 38 minutes 42 seconds (literally forgot to add the -1 and took 10 minutes
trying to figure out why the array was off by one lol)
'''

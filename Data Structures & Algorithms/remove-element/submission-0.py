class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_array = []
        p_in_new = 0
        for i in range(len(nums)):
            if nums[i] != val:
                new_array.append(nums[i])
        #then put that shit in old array
        for i in range(len(new_array)):
            nums[i] = new_array[i]
        return len(new_array)



'''
given: array: nums, int: val

goal: remove all occurences of val in numsIN PLACE

Input: nums = [3,2,2,3], val = 3

Output: k = 2, nums = [2,2,_,_]

[3,2,2,3]
            *
[_, 2, _, 2, 3, 3]

keep going until reached original size

keep track of how many numbers we shifted (how many times we shifted numbers)

shift each number by that amount (for the original length only)
remember to keep track of k (can get by subtracting shift amount from length of nums)

shift = 0
for i in range(len(nums)):
    if nums[i] == val:
        nums[i] = None
        shift+=1
    
for i in range(len(nums)):
    
    ---------------
new array

for loop:
    skip three, take whats not equal to three and put in new array
    when u reach end, take new array and equal it to old array
    keep track of 


'''
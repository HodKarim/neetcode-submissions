class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        new_array = []
        for i in range(len(nums)):
            if nums[i] != val:
                new_array.append(nums[i])
            else:
                continue

        for j in range(len(new_array)):
            nums[j] = new_array[j]
        return len(new_array)
'''
given: integer aray nums and integer val
goal: remove all occurences of val in nums in place

since order of elems can be changed, 

[0,1,2,2,3,0,4,2]
     i            

for i in range(nums, length)

keep going thru array til we hit val
when we hit val in nums[i], swap it with nums[j]
decrement j and continue. 

make new array. copy it back into nums. 


'''
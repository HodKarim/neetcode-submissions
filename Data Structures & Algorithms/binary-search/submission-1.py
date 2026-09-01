class Solution:
    def search(self, nums: List[int], target: int) -> int:

        i = 0
        j = len(nums)-1
        while i<=j:
            middle = (j+i) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                i = middle + 1
            else:
                j = middle - 1
                
        return -1     

'''
given array of distinct ints nums sorted in ascending order and target

[-1,0,2,4,6,8]   look for 3



the middle is len(nums)-1//2?

i = 0
j = len(nums)-1


while i<j:
    middle = (j+i) // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] < target:
        i = middle + 1
    else:
        j = middle - 1

return -1
'''
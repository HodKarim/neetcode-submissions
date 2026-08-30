class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        mid_index = (len(nums)-1) // 2
        i = 0
        j = len(nums)-1

        while i <= j:
            if nums[mid_index] < target:
                #set the left pointer to the middle
                i = mid_index + 1
                mid_index = (j+i) // 2

            elif nums[mid_index] > target:
                #set the right pointer to middle
                j = mid_index - 1
                mid_index = (j+i) // 2
            else:
                return mid_index #means its correct
        return -1

'''
given array of elements nums sorted and given target

implement function to search for target within nums. if there, return index else -1



[-1,0,2,4,6,8]  0
 ^     ^


'''
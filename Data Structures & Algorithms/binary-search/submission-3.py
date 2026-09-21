class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1

        while i <= j:
            mid = (j + i) // 2 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target: #must b on the right
                i = mid + 1
            else:
                j = mid - 1
        return -1
'''
given: array of distinct ints, sorted (Asc), target int

search for target. if not, return -1


[-1,0,2,4,6,8], target = 4
i
             j



'''
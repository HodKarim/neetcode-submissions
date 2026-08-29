class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        i = 1
        j = len(nums) - 1
        result = []

        check_duplicates = float('inf')
        for k in range(0,len(nums)-2):
            if nums[k] == check_duplicates:
                continue
            check_duplicates = nums[k]
            i=k+1
            j=len(nums)-1

            while i<j:
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    j-=1
                else:
                    i+=1
        return result

'''

[-4,-1,-1,0,1,2]

 ^  
    ^
              ^




ensure in the inner while loop that i and j never touch. if they do that means that
isnt a solution
also make sure that the first pointer in the outer loop is never the same. so we save it
in check_duplicate and see if the current nums[i] = equal to it.



'''
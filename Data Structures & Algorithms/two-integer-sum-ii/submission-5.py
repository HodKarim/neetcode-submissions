class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers)-1

        while i < j:
            ans = numbers[i] + numbers[j]

            if ans > target:
                j-=1
            elif ans < target:
                i+=1
            else:
                return [i+1,j+1]
'''
given array of ints numbers sorted 

return indices of 2 nums st they add up to target 

[1,2,3,4], target = 3
i
       j

since its sorted we keep 2 running pointers

the loop should run until they hit each other

add nums[i] and nums[j]. 

if its bigger than target, increase i

if smaller, decrease j

keep going til they r equal.




'''
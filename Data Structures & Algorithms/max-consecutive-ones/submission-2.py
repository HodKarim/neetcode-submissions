class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxx = 0

        '''
        i = 0
        if nums[0] == 1
        count+=1

        '''
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                if maxx < count:
                    maxx = count
                    count = 0
                else:

                    count = 0
        if maxx < count:
            maxx = count
        return maxx

'''
given: binary array nums

goal: return the max # of consecutive 1's in array

[1,1,0,1,1,1]
            ^
count = 2
max

if we hit a 0:
    max = count (only if count is bigger than max)

basically:
for loop from 0 to end of array
    everytime we hit a one, increment count
    until we hit 0, when we hit 0 we do the if statement
    set count back to 0
'''


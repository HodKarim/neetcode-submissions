class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer_list = []
        answer = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                #loop thru all numbers except nums[i] and multiply each out
                if i !=j:
                    answer *= nums[j]
            answer_list.append(answer)
            answer = 1
        return answer_list
'''
given an integer array nums, return an array output where output[i] is product of all emenets of nums except nums[i]

so basically:

#naive approach:

answer_list = []
answer = 1
for i in range(len(nums)):
    for j in range(len(nums)):
        #loop thru all numbers except nums[i] and multiply each out
        if i !=j:
            answer *= nums[j]
    answer_list.append(answer)
    answer = 1


[1,2,4,6]
i 
j

i = 0
j = 0
skip

i=0
j = 1
answer = 1 * 1 = 1

i = 0
j = 2
answer = 1 * 2 = 2
'''
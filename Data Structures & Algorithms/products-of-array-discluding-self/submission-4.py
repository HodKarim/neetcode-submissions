class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix
        prefix_multiple = []
        for i in range(len(nums)):
            if i == 0:
                prefix_multiple.append(nums[i]) #starting one
                prefix = nums[i]
            else:
                prefix*=nums[i] #1*1 
                prefix_multiple.append(prefix)

        suffix_multiple = [0]*len(nums)

        #[1,2,4,6]
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix = nums[i]
                suffix_multiple[i] = postfix
                
            else:
                postfix*=nums[i]
                suffix_multiple[i] = postfix

        #now for making array

        answer = []
        for i in range(len(nums)):
            if i==0:
                answer.append(suffix_multiple[i+1])
            elif i==len(nums)-1:
                answer.append(prefix_multiple[i-1])
            else:
                ans = suffix_multiple[i+1] * prefix_multiple[i-1]
                answer.append(ans)

        return answer   
        '''
        given integer array nums
        return array output where output[i] is product of all elements of nums except nums[i]
        constraint: must be in O(n) time and cannot use division operator!

        example:

        [1,2,4,6]

        result:

        [48,24,12,8]

        how to get this:

        48 is basically the product of a sub array from i=1 to i=3
        24 is product of sub arrays i=0 and i=2 to i=3

        compute prefix product:

        1  1*2 1*2*4  1*2*4*6
        [1,  2,   8,    48]

        compute postfix product:

        6*4*2*1 6*4*2 6*4 6
        [48,    48,   24,  6]

        so right before that index. postfix[i+1] * prefix[i-1]


        so now we create both the postfix and prefix using diff arrays.

        then we compute the final answer using postfix[i+1] * prefix[i-1]

        #prefix
        prefix = 1
        prefix_multiple = []
        for i in range(len(nums)):
            if i == 0:
                prefix_multiple.append(nums[i]) #starting one
            else:
                prefix*=nums[i] #1*1 
                prefix_multiple.append(prefix)

        suffix_multiple = []

        #[1,2,4,6]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                suffix_multiple.append(nums[i])
            else:
                postfix*=nums[i]
                suffix_multiple.append(postfix)

        #now for making array

        answer = []
        for i in range(len(nums)):
            if i==0:
                answer.append(suffix_multiple[i+1])
            elif i==len(nums)-1:
                answer.append(prefix_multiple[i-1])
            else:
                ans = suffix_multiple[i+1] * prefix_multiple[i-1]
                answer.append(ans)

        return answer
        '''
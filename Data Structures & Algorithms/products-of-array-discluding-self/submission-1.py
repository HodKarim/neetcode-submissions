class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            count = 1
            for j in range(len(nums)):
                #if its the one we're in, pass
                if i == j:
                    continue
                else:
                    count = count * nums[j]
            output[i] = count
        return output
'''
[1,2,4,6]
i = 1
j = 0
count = 1

i = j, continue

i = 0
j = 1
count = 1
count  = 1 * nums[1] = 1 * 2 = 2

i = 0
j = 2
count  = 2
count = count * nums[2] = 2 * 4 = 8
'''

'''
given:
integer array (nums)

goal: 
return an array (output) where output[i] is the product of all elements of nums except nums[i]

example:

[1,2,4,6] <--- nums

nums[0] = 1

output[0] = 2 * 4 * 6 = 48

solution:

nums[i] 
[1,2,4,6]

#initialize output array
output = []

for i in range(len(nums)):
    count = 1
    for j in range(len(nums)):
        
        #if its the one we're in, pass
        if i == j:
            continue
        else:
            count = count * nums[j]
    output[i] = count

return output
'''







































'''
        # create output list with 1s
        # each spot will eventually store the product except itself
        output = [1] * len(nums)

        # prefix will store product of everything before current index
        prefix = 1

        # go left to right
        for i in range(len(nums)):
            # put prefix product into output[i]
            # this means product of all numbers before nums[i]
            output[i] = prefix

            # update prefix by multiplying current number
            prefix *= nums[i]

        # postfix will store product of everything after current index
        postfix = 1

        # go right to left
        for i in range(len(nums) - 1, -1, -1):
            # multiply current output[i] by postfix
            # output[i] already has left side product
            # postfix gives right side product
            output[i] *= postfix

            # update postfix by multiplying current number
            postfix *= nums[i]

        # return final answer
        return output


        """
        Pattern Type: Prefix + Postfix product pattern

        need product of all numbers except current number, but cannot use division
        so split the problem into left side product and right side product

        Time Complexity:
        O(n), because go thru nums two times

        Space Complexity:
        O(1), because output list does not count as extra space.
        only using prefix and postfix variables

        How long it took: 35 minutes
        """
'''
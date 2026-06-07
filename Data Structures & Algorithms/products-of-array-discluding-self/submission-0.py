class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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
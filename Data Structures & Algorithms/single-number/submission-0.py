class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result ^ num
        return result
        '''
        given: non empty array of numbers (nums)
        every int is in there twice except for 1

        return the integer that appears only once
        must be O(n) and O(1) space

        [7,6,6,7,8]

        for each element in the array, we XOR it with result.

        result = 0

        result ^ nums 

        when we return result, itll be the only number that does not have a duplicate.








        bit operations:

        and: &
        or: ^
        
        '''
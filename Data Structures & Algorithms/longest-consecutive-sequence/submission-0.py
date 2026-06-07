class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            #start sequence only if this is the first number
            if num - 1 not in num_set:
                length = 1
                current = num

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


'''
Logic:
put all numbers into a set for O(1) lookups
iterate through each num in set
only start counting if the previous number (num - 1) doesnt exist (found start of sequence)
keep checking if the next number exists and extend the sequence
track the longest sequence length seen so far
return the longest length

Pattern:
Hash Set

Time Complexity:
O(n)
each number is visited at most once across all sequence expansions

Space Complexity:
O(n)
we store all numbers in a hash set

Time to complete problem:
12 minutes
'''
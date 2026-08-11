class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 == 1:
                count+=1
            n = n >> 1
        return count



'''
given: unsigned integer n

goal: return the number of 1 bits in the binary representation

assume n is non negative int

so basically we do the following

00000000000000000000000000010111
AND
00000000000000000000000000000001

== 1

shift n to the? right to get rid of the int



'''
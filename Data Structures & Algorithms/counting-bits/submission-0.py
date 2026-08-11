class Solution:
    def countBits(self, n: int) -> List[int]:
        array = []
        for i in range(0,n+1):
            count = 0
            number = i
            while number > 0:
                if number & 1 == 1:
                    count+=1
                number = number >> 1
            array.append(count)
        return array

'''
given integer n

goal: count number of 1s in binary representation for every number in range [0,n]

so given 4, 
00000 0
00001 1
00010 2
00011 3
00100 4




'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] > target: #like 9+2 = 11
                #decrement j
                j-=1
            elif numbers[i] + numbers[j] < target: #increment i
                i+=1
            else:
                return [i+1,j+1]
'''
two integer sum II


given: array of insts numbers sorted in increasing order (1,2,3..)

return the indices of two numbers that add up to target number and the first index must be larger than the second

O(1) addition space 
target = 5
[2,3,4,5,6,7,8,9]
 ^             ^

#remember to return i+1, j+1


'''
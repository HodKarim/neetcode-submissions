class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0
        j = len(numbers)-1

        while i<j:
            if numbers[i] + numbers[j] >target:
                j-=1
            elif numbers[i] + numbers[j] < target:
                i+=1
            else:
                return [i+1,j+1]

'''
given an array of ints nums sorted in increasing order
return indices (1 indexed) of 2 numbers [i1, i2] s.t they add up to target and i1 < i2

cannot be equal

[1,2,3,4]  
   ^ ^

4+1 = 5
3+1=4 bigger, decrement j

brute force is O(n^2)



'''
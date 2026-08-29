class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1

        max_area = float('-inf')

        while i<j:
            area = min(heights[i], heights[j]) * (j-i)

            if area > max_area:
                max_area = area
            
            if heights[j] < heights[i]:
                j-=1
            else:
                i+=1
        return max_area        

'''
given integer array heights where heights[i] is that bars height

can choose any 2 pars to form a container. return max amount of water a container can hold.

note: cant sort


[1,7,2,5,4,7,3,6]
   ^
               ^

height = min(1,6) = 1
widrth = 7-0 = 7 
maximum = 7*1 = 0



brute force: check all. 

first, how to calculate whow much water?

height = min(i,j) and width = j-i. multiply them





'''
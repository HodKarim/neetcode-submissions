class Solution:

    def trap(self, height: List[int]) -> int:
        stack = []
        total_water = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break

                left = stack[-1]
                width = i - left - 1

                bounded_height = (
                    min(height[left], height[i])
                    - height[bottom]
                )

                total_water += width * bounded_height

            stack.append(i)

        return total_water
'''
given array of non neg ints height that represent an elevation map

each value represents the height of a bar which has a width of 1

return the total amount of ater that can be trapped between the bars

[0,2,0,3,1,0,1,3,2,1]
   ^   
monotonic stack

mon_stack = []
curr_height = 0
total_water = 0
for i in range(len(height)):
    if height[i] == 0:
        continue
    
    if curr_height == 0:
        curr_height = height[i]
    else:
        if height[i] < curr_height:
            mon_stack.append(height[i])
        else: #if its equal or bigger than the current height we have to now get water 
            water = 0
            while mon_stack:
                water += ((min(height[i], curr_height) - mon_stack[-1])
                mon_stack.pop()
            
            curr_height = 0
            total_water += water
        
the max it can be is the smaller of the two heights

height - the other heigh





we need to start the stack process
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        maxx_left_arr = []
        maxx_L = 0
        for i in range(len(height)):
            if i == 0:
                maxx_left_arr.append(0)
                maxx_L = height[i]
            else:
                maxx_left_arr.append(maxx_L)
                if height[i] > maxx_L:
                    maxx_L = height[i]

        maxx_right_arr = []
        maxx_R = 0
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                maxx_R = height[i]
                maxx_right_arr.append(0)
            else:
                maxx_right_arr.append(maxx_R)
                if height[i] > maxx_R:
                    maxx_R = height[i]
        maxx_right_arr.reverse()
        res = 0
        for i in range(len(height)):
           res += max(0, min(maxx_right_arr[i], maxx_left_arr[i]) - height[i])
        
        return res


'''
get the max height on the left and right side

then compute min(L,R) - height[i] for each position


#max on the left:



[0,2,0,3,1,0,1,3,2,1]

LEFT 
[0,0,2,2,3,3,3,3,3,3]

RIGHT
[0,1,2,3,3,3,3,3,3,3]
'''
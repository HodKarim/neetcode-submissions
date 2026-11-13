class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1

        max_area = float('-inf')

        while i < j:
            width = j - i
            length = min(heights[i], heights[j])
            curr_area = width * length

            if curr_area > max_area:
                max_area = curr_area
            
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left pointer starts at beginning of array
        left = 0

        # right pointer starts at end of array
        right = len(heights) - 1

        # stores the biggest area found so far
        max_water = 0

        # keep going while left is before right
        while left < right:
            # width is the distance between the two bars
            width = right - left

            # height is limited by the shorter bar
            # water spills over the shorter side
            curr_height = min(heights[left], heights[right])

            # area is width times the shorter height
            area = width * curr_height

            # update max_water if current area is bigger
            max_water = max(max_water, area)

            # move the pointer with the smaller height
            # moving the taller one will not help because water is limited by shorter bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        # return the biggest amount of water found
        return max_water


        """
        Pattern Type: Two Pointers pattern.

        need to find max water using two bars.
        start with widest container, then move the smaller height inward.
        smaller height is the limit, so moving it gives a chance to find a taller bar.

        Time Complexity:
        O(n), because each pointer moves through the array at most once

        Space Complexity:
        O(1), because only using two pointers and a few variables

        How long it took: 30 minutes

        Logic:
        start left at index 0 and right at last index.
        calculate width as right - left.
        calculate height using the smaller of the two bars.
        area = width * height.
        update max_water if area is bigger.
        move the pointer with the smaller height inward.
        keep doing this until the pointers meet.
        """
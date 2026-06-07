class Solution:
    def trap(self, height: List[int]) -> int:
        #left pointer starts at start of array
        left = 0

        # right pointer starts at end of array
        right = len(height) - 1

        # stores tallest bar seen from left side
        l_max = height[left]

        # stores the tallest bar seen from right side
        r_max = height[right]

        # stores total trapped water
        water = 0

        # keep going while left is before right
        while left < right:
            # move side w the smaller max height
            # water limited by the shorter side
            if l_max < r_max:
                # move left pointer inward
                left += 1

                # update if current bar is taller
                l_max = max(l_max, height[left])

                # water trapped jere is left_max - current height
                water += l_max - height[left]

            else:
                # move right pointer inward
                right -= 1

                # update right_max if current bar's taller
                r_max = max(r_max, height[right])

                # water trapped here is right_max - current height
                water += r_max - height[right]

        # return total trapped water
        return water


        """
        Pattern Type: Two Pointers pattern

        need to calculate how much water can sit above each bar
        water depends on smaller wall between left side max and right side max
        use two pointers so we do not need extra arrays

        Time Complexity:
        O(n), because each pointer moves through the array at most once

        Space Complexity:
        O(1), because only using pointers and variables

        How long it took: 39 minutes

        Logic:
        start left at index 0 and right at last index????
        keep track of left_max and right_max using specific indexes
        move the side with the smaller max because that side limits the water
        if left_max is smaller, move left and add left_max - height[left]
        if right_max is smaller, move right and add right_max - height[right]
        keep adding trapped water until pointers meet
        """
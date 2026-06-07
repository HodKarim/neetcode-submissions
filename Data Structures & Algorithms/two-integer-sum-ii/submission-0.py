class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # left pointer starts at beginning of array
        left = 0

        # right pointer starts at end of array
        right = len(numbers) - 1

        # keep going while left is before right
        while left < right:
            # get sum of the two pointer values
            curr_sum = numbers[left] + numbers[right]

            # if sum equals target, return 1-indexed positions
            if curr_sum == target:
                return [left + 1, right + 1]

            # if sum is too small, move left pointer right
            # this makes the sum bigger because array is sorted
            elif curr_sum < target:
                left += 1

            # if sum is too big, move right pointer left
            # this makes the sum smaller because array is sorted
            else:
                right -= 1


        """
        Pattern Type: Two Pointers pattern.

        array is already sorted, so use one pointer at start and one pointer at end.
        if sum is too small, move left pointer to get bigger number.
        if sum is too big, move right pointer to get smaller number.

        Time Complexity:
        O(n), because each pointer moves through the array at most once

        Space Complexity:
        O(1), because only using two pointers and no extra data structure

        How long it took: 25 minutes

        Logic:
        start left at index 0 and right at last index.
        add numbers[left] + numbers[right].
        if sum equals target, return their positions plus 1 because answer is 1-indexed.
        if sum is less than target, move left right to increase sum.
        if sum is greater than target, move right left to decrease sum.
        """
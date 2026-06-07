class Solution:
    def isPalindrome(self, s: str) -> bool:
        # left pointer starts at beginning of string
        left = 0

        # right pointer starts at end of string
        right = len(s) - 1

        # keep checking while pointers have not crossed
        while left < right:
            # if left char is not a letter or number, skip it
            while left < right and not s[left].isalnum():
                left += 1

            # if right char is not a letter or number, skip it
            while left < right and not s[right].isalnum():
                right -= 1

            # compare both chars after making them lowercase
            # if they are different, it is not a palindrome
            if s[left].lower() != s[right].lower():
                return False

            # move both pointers toward the middle
            left += 1
            right -= 1

        # if all characters matched, it is a palindrome
        return True


        """
        Pattern Type: Two Pointers pattern.

        need to compare characters from both ends of the string.
        left pointer starts at beginning, right pointer starts at end.
        skip anything that is not a letter or number because problem says to ignore them.

        Time Complexity:
        O(n), because each character is checked at most once

        Space Complexity:
        O(1), because only using two pointers and no extra list/string

        How long it took: 20 minutes

        Logic:
        move left and right pointers toward the middle.
        skip non-alphanumeric characters.
        compare lowercase versions of both characters.
        if any pair does not match, return False.
        if all valid characters match, return True.
        """
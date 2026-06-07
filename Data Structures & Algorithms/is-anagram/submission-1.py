class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if  two strings have different lengths, they cannot be anagrams
        if len(s) != len(t):
            return False

        # create two dicts to count how many times each character appears in each string
        countS = {}
        countT = {}

        # loop thru both strings at the same time
        for i in range(len(s)):
            # count chars from string s
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # count chars from string t
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # if both dicts same, both strings have exact same characters w  exact same counts
        return countS == countT

        """
        Pattern Type: Hash Map pattern.

        count how many times each character is in both strings.

        Time Complexity:
        O(n), because we loop through the strings once

        Space Complexity:
        O(1), the strings only contain lowercase letters so there's 26 different chars stored
        otherwise,  space complexity would be O(n)

        How long it took: 15 minutes, 3 min for comments
        """
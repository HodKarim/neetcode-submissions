class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create dict where:
        # key   = a character count pattern for a word
        # value = a list of words that match that pattern
        anagram_groups = {}

        # go thru each word in input list
        for word in strs:
            # since strs[i] only contains lwrcase letters, use list size 26 to count each char
            count = [0] * 26

            # count how many times each char appears in the word
            for char in word:
                # ord(char) - ord("a") converts a letter into an index
                # eg:
                # "a" becomes 0
                # "b" becomes 1
                # "c" becomes 2
                count[ord(char) - ord("a")] += 1

            # lists cannot be dictionary keys because they are mutable: convert the count list into a tuple
            key = tuple(count)

            # if this character-count pattern has not been seen before, create new empty list for it
            if key not in anagram_groups:
                anagram_groups[key] = []

            # ddd current word to the group with the same pattern
            anagram_groups[key].append(word)

        # return only the grouped lists, not dictionary keys
        return list(anagram_groups.values())


        """
        Pattern Type: Hash Map pattern with character frequency counting.
        anagrams have the same characters with the same counts, even if the letters are in a different order.
        EG: "act" and "cat" both have 1 "a", one "c", and one "t", so they belong in same group.

        Time Complexity:
        O(n * k), where n is the number of strings and k is the average length
        of each string: visit every character in every word once

        Space Complexity:
        O(n * k), because we store all the strings inside the output groups
        The dictionary also stores keys, but each key has a fixed size of 26,
        so the main extra space is the grouped output

        How long it took: 32 minutes, 3 minutes for comments
        """
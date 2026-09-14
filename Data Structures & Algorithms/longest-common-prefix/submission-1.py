class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        compare = strs[0]

        for i in range(1, len(strs)):
            string = ""
            word = strs[i]

            length = min(strs[i], compare)
            for j in range(len(length)): #compare
                if word[j] == compare[j]:
                    string = string + word[j]
                else:
                    break
            #now new word to compare is whats left from string
            compare = string

        return compare
'''
given array of strings strs.

return the longest common prefix of all strings

if none, return ""

strs = ["bat","bag","bank","band"]




take the first element in the list and start with that.




'''
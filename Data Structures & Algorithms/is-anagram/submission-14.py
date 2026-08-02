class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = sorted(list(s))

        t_list = sorted(list(t))

        if s_list == t_list:
            return True
        else:
            return False
'''
given: 2 strings, s and t

goal: return true if two strings are anagrams (both strings have same characters)
return false otherwise

solution:

iterating thru one and seeing if the letters of it are in the other

sorting both (O(n log n))

comparing both strings


'''
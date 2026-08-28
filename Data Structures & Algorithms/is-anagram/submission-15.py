class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        ss = "".join(s_sorted)
        tt = "".join(t_sorted)

        if ss == tt:
            return True
        else:
            return False

'''
given two strings s and t

goal: return true if both are anargrams of each other (same characters), else return false

sort both words and compare.


'''
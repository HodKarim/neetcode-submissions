class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        ss = "".join(sorted(s))
        tt = "".join(sorted(t))

        if ss == tt:
            return True
        else:
            return False

'''
given two strings s and t

goal: return true if both are anargrams of each other (same characters), else return false

sort both words and compare.


'''
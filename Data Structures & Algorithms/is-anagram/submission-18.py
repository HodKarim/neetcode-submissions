class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        ss = list(s)
        tt = list(t)

        ss.sort()
        tt.sort()

        if ss == tt:
            return True
        else:
            return False
'''
valid anagram

given 2 strings return if the length t == len s

additionally, return if no letter in the first string is NOT present in the second string


this means using the counter variable and seeing if they r equal?

also can set both as lists, sort the lists, and then see if they r equal to each other
'''
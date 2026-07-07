class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_list = list(s)
        t_list = list(t)

        tt = sorted(t_list)
        ss = sorted(s_list)

        if tt == ss:
            return True
        else:
            return False
                
        




'''
given: two strings, s and t.
goal: return true if strings are anagrams of each other. otherwise, return false

first, if they are not equal length, just return false.

if they are equal length, continue

we can sort both strings and then after, see if they are equivalent

'''

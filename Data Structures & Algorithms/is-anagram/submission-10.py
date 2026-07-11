class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = "".join(sorted(s))
        t_sort = "".join(sorted(t))

        if s_sort == t_sort:
            return True
        else:
            return False
        




'''
Given: strings s and t
Goal: return true if strings have exact same letters & equal length. otherwise, false


example:

s = racecar, t = carrace

solution:
sort both strings and compare them.




'''

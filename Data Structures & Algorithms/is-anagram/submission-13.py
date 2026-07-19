class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

'''
given: two strings, s and t
goal: return true if string are anagrams of each other, otherwise return false

solution:

optimized:

python sorted()

O(1)
O(1)


'''
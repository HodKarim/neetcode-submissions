class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)
        tt = list(t)

        sss = sorted(ss)
        ttt = sorted(tt)

        ssss = "".join(sss)
        tttt = "".join(ttt)

        if ssss == tttt:
            return True
        else:
            return False
'''
given 2 strings, return true if they r anagrams

basically sort them and see if equal


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        giuven 2 strings: s and t, return true if strings are anagrams
        otherwise, false

        a r c e c a r
        i           j 
    for i in range(len(s))
        for j in range(lens(s))
            if j < i:
                #swap
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                

            '''
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        
        if t_list == s_list:
            return True
        else:
            return False
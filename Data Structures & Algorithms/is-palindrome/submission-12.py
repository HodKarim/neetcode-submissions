import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        new_s = re.sub(r"[^a-zA-Z0-9]", "", s)
        j = len(new_s) - 1  

        while i < j:
            if new_s[i].lower() == new_s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True
'''
given a string s, teturn true if its a palindrom, or else return false

string read the same forward and backwards


so we use 2 pointers and move them closer and closer checking if they are equal


basically, for half of the length, as long as they are equal we keep checking

"Was it a car or a cat I saw?"

the spaces are also an issue. 

'''
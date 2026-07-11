class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checking_map = {}

        for i in range(len(strs)):
            anagram = "".join(sorted(strs[i]))
            if anagram in checking_map:
                #get value list and append to end of value list
                valuee = checking_map[anagram] #should be a list
                valuee.append(strs[i])
            else:
                checking_map[anagram] = [strs[i]]
        return list(checking_map.values())


'''
given: array of strings (strs)
goal: group all anagrams together into sublists (return output in any order)
output: list of lists

soltution:

hashmap: key = sorted letter

["act","pots","tops","cat","stop","hat"]

hashmap:
key = sorted word
value = list of anagram for that word

checking_map = {}

for i in len(strs):
    anagram = strs[i].sort()
    if anagram in checking_map (as a key):
        get value list and append to end of the value list
    else:
        make anagram a key in the checking_map and make the value strs[i]

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checking_map = {}

        for i in range(len(strs)):
            checking_word = "".join(sorted(strs[i]))

            if checking_word in checking_map:
                checking_map[checking_word].append(strs[i])
            else:
                checking_map[checking_word] = [strs[i]]

        #take hashmap and turn it into list of lists

        listt = []
        for value in checking_map.values():
            listt.append(value)
        return listt

'''
given: array of strings strs
goal: group all anagrams together into sublists

example:

strs = ["act","pots","tops","cat","stop","hat"]

solution:

act, opst, opst, act

sort word, check if words already in hashmap (checj key), if so, append to list value

{"sorted word": list of words that are anagram to sorted word}

checking_map = {}

for i in range(len(strs)):
    checking_word = "".join(sorted(strs[i]))

    if checking_word in checking_map:
        checking_map[checking_word] = checking_map[checking_word].append(strs[i])
    else:
        checking_map[checking_word] = [strs[i]]

#take hashmap and turn it into list of lists

listt = []
for index, value in checking_map:
    lists.append(checking_map[index])
return listt
'''


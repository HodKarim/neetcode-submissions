class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}

        for i in range(len(strs)):
            sorted_strs = "".join(sorted(strs[i]))
            if sorted_strs in dictt:
                dictt[sorted_strs].append(strs[i])
            else:
                dictt[sorted_strs] = [strs[i]]
        answer = []
        for value in dictt.values():
            answer.append(value)
        return answer
'''
given: arr of string
goal: group all anagrams together into sublists 
returned in any order

soln: for loop traversing thru input and checking if
sorted word is already in dict.

if not in dict, have sorted word as the key and
unsorted in the value list

if in dict, append to value list 
'''


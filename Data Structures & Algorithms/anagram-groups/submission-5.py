class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) in anagram_map:
                #append strs[i] to the value of the key

                element = anagram_map["".join(sorted(strs[i]))]
                element.append(strs[i])
                anagram_map["".join(sorted(strs[i]))] = element
            else:
                anagram_map["".join(sorted(strs[i]))] = [strs[i]]
        answer = []
        for value in anagram_map.values():
            answer.append(value)
        return answer

'''
given: array of strings (strs) 
goal: group all anagrams together into sublists (list of lists output)

solution:
to check if anagram, must sort word and see if equal

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

hashmap where the key is sorted version and the value would be an array of all the words that are anagrams
of that sorted word

sorted_list = []
anagram_map = {}
for i in range(len(strs)):
    sorted_list.append("".join(sorted(strs[i]))) #might need to change

for i in range(len(strs)):
    if "".join(sorted(strs[i])) in anagram_map:
        #append strs[i] to the value of the key

        element = anagram_map.value("".join(sorted(strs[i])))
        element.append(strs[i])
        anagram_map.value("".join(sorted(strs[i]))) = element
    else:
        anagram_map["".join(sorted(strs[i]))] = [strs[i]]


'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for i in range(len(strs)):
            sorted_strs = "".join(sorted(strs[i]))

            if sorted_strs in anagrams:
                value = anagrams[sorted_strs]
                value.append(strs[i])
            else:
                anagrams[sorted_strs] = [strs[i]]

        answer = []

        for value in anagrams.values():
            answer.append(value)
        return answer
'''
given array of strings, group anagrams together into sublists.

can return output in any order

sort each word and see if it matches the key. if no key exists, make one



'''
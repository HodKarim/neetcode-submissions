class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        checking = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if sorted_word in checking:
                words = checking[sorted_word] #value list
                words.append(strs[i])
                checking[sorted_word] = words # maybe can b done in 1 operation
            else:
                checking[sorted_word] = [strs[i]] #new

        result = []
        for value in checking.values():
            result.append(value)

        return result
 
        '''
        given array of strings strs, group all anagrams together into sublists

        basically we sort the words and see which ones are spelled the same.

        to match the sorted words with their unsorted words, use hashmap for mapping and to keep O(1) time complexity for lookup.

        must check if sorted word is already in hashmap. 
        if it is, append og word to value list
        else, add to hashmap


        '''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for strr in strs:
            sorted_str = "".join(sorted(strr))
            if sorted_str in anagrams:
                #we're going to add/append og str to the list of values
                anagrams[sorted_str].append(strr)
            else:
                #add the sorted word as a key and have a list with the unsorted word as a value
                anagrams[sorted_str] = [strr]
        result = []  
        for value in anagrams.values():
            result.append(value)
        return result
'''
given an array of strings strs

goal: group all anagrams together into sublists (aka return a list of lists)

["act","pots","tops","cat","stop","hat"]

anagrams = {"act:[act,cat], "opst": [tops, stop, pots], "aht": [hat]}
make a list with all the values (for loop to do so)

iterate over the array. 
sort the word. after sorting, see if it exists in the hashmap. if it already exists, add the unsorted version
to the list for the values. 
---------------

anagrams = {}
for str in strs:
    sorted_str = sorted(str)
    if sorted_str in anagrams:
        #we're going to add/append og str to the list of values
        anagrams[sorted_str].append(str)
    else:
        #add the sorted word as a key and have a list with the unsorted word as a value
        anagrams[sorted_str] = [str]
result = []  
for value in anagrams.values():
    result.append(value)
return result


'''
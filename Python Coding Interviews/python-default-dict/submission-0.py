from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    freq = defaultdict(int)
    for i in range(len(s)):
        freq[s[i]] += 1
    return freq
'''
take string and return dict where keys are chars and values are # of times it appears in string
'''

def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    freq = defaultdict(list)
    for sublist in nums:
        freq[sublist.pop(0)] += sublist
    return freq
    
'''
takes list of list of ints and returns dict where keys are first elem of each list
and values are rest of elems in list
'''


# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))

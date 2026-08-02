class Solution:
    
    #counter collection
    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        #number 1: 1 times, number 2...

        listt = []
        for key, value in freq_counter.items():
            listt.append((value, key)) #as a tuple, o(n) time

        heapq.heapify(listt)

        ans_as_tuple = heapq.nlargest(k, listt)
        
        ans = []

        for freq, num in ans_as_tuple:
            ans.append(num)
        return ans

'''
given integer array nums and integer k, return the k most frequent elements in the array

for example, return the 2 most frequent element

[1,2,2,3,3,3]

lets do this: make a tuple where the first element is how frequent and the second element is 
the # itself.

[(1,1), (2,2), (3,3)]

then we sort using heapsort? and use nlargest to return.

this should be O(n log n) time.

use counter?

freq_counter = Counter(nums)
#number 1: 1 times, number 2...

listt = []
for key, value in freq_counter.items():
    listt.append((value, key)) #as a tuple, o(n) time

heapq.heapify(listt)

return heapq.nlargest(k, listt)



'''
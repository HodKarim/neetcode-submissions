from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums) #gives is {1:1, 2:2, 3:3}

        #put in an array as a tuple?

        arr = []
        for key, value in count.items():
            arr.append((value, key)) #gives count, element

        heapq.heapify(arr)

        ans = heapq.nlargest(k, arr) #will give us an array like [(3,3), (2,2)..]

        result = []
        for tuple1, tuple2 in ans:
            result.append(tuple2) #this is wrong

        return result
'''
given int array (nums), integer k

goal: return k most frequent elements in the array.


optimal approach:

heap since heaps provice the nlargest function that returns the n largest elements


'''
class Solution:
    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) #gives us {3:3, 2:2, 1:1}

        arr = []
        #for loop turning hashmap into tuples
        for element, freq in counter.items():
            arr.append((freq, element)) #gives us [ (3,3), (2,2), (1,1)]
        
        heapq.heapify(arr) #

        arr2 = heapq.nlargest(k, arr) #gives us [(3,3), (2,2)]

        #now we need a for loop to extract the second index of the tuples and add them to an arr
        arr3 = []

        for element in arr2:
            arr3.append(element[1]) #how do i get the second element in each tuple?
        return arr3
        


'''
top k elements ---> heaps nlargest
[1,2,2,3,3,3]

heapq.nlargest(heap, k)
[3,3,3]

heaps allow for priority queues

using tuples:
[how many times the element is in the array, element itself]

Counter in python: 

hashmap --> {3:3, 2:2, 1:1}

for loop to turn these into tuples (new array)

heapify using new array

use heapq.nlargest







'''
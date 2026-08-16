class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #initializes object given integer k and stream of ints nums
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        #adds integer val to stream and gives the kth biggest integer
        self.nums.append(val)
        heapq.heapify(self.nums)
        result_array = heapq.nlargest(self.k, self.nums)
        return result_array[-1]

        
'''
design class that finds the kth biggest number in stream of values w duplicates
so basically add the integer, heapify the new array
the kth largest integer, hmmmm

nlargest element gives the n largest elements in a heap. so all i gotta do is return [-1] of it
'''
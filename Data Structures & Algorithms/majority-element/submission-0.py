from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = Counter(nums) #this gives how frequent each elem is. element first, freq 2nd

        biggest = -1
        number = -1
        for key, value in counter.items():
            #compare each value with biggest. if the value is bigger than biggest, 
            #store its key in number and value in biggest

            if counter[key] > biggest:
                number = key
                biggest = value

        return number

'''
given array nums of size n, return the majority element

returns more than n/2 floor times



'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        checking = {}
        for i in range(len(nums)):
            subtracted_elem = target - nums[i]
            checking[subtracted_elem] = i


        for i in range(len(nums)):
            if nums[i] in checking and checking[nums[i]] != i:
                return [min(i, checking[nums[i]]), max(i, checking[nums[i]])] 

'''
given array of ints nums and int target
goal is return indices i and j st nums[i] + nums[j] == target and i != j

naive approach (O(n^2)): nested for loop checking each

[3,4,5,6]
  i  j
3+4 = 7
3+5 = 8
3+6 = 9
4+5...


constraint: i and j cannot be equal or else we can get thr wrong answer (3 + 3 = 6)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]

O(n):

since we already have target, we can precompute the answer and just traverse through them instead

eg:

[3,4,5,6], target = 7

7-3 = 4. 4 is in the array. 
7-4 = 3
7-5 = 6
7-6=1

checking = {}
for i in range(len(nums)):
    subtracted_elem = target - nums[i]
    checking[subtracted_elem] = i

so we get {4: 0, 3:1, 6:2, 1:3}

now traverse thru array and see if the elems are in it

for i in range(len(nums)):
    if nums[i] in checking and checking[nums[i] != i]:
        return [min(i, checking[nums[i]]), max(i, checking[nums[i]])]

store the number itself as the key and the index that was subtracted as the value

'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = 0
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                for j in range(i+1, len(arr)):
                    if maxx < arr[j]:
                        maxx = arr[j]
                arr[i] = maxx
                maxx = 0
        return arr



'''
given array arr
goal: replace every element in array with greatest element among th elements to its right
replace last elem with -1

[2,4,5,3,1,2]
     i

goes from 0 to 6

at arr[0]:
    start ar arr[0] and compute the max
    once we get max, change arr[0] to max

10^3, accepts O(n^2)

'''
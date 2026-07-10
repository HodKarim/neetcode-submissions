from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    #returns index of first occurence of # 7 in list nums, or -1 if not found
    for i, n in enumerate(nums):
        if n == 7:
            return i
    return -1


def get_dist_between_sevens(nums: List[int]) -> int:
    #return distance between first and second occurence of # 7 in list nums
    flag = 0
    for i, n in enumerate(nums):
        if n == 7 and flag == 0:
            x = i
            flag = 1
        elif n == 7 and flag == 1:
            y = i
            break
    return y - x



'''
Implement the following functions using enumerate():

get_index_of_seven(nums: List[int]) -> int that returns the index of the first occurrence of the number 7 in the list nums, or -1 if 7 is not found.
get_dist_between_sevens(nums: List[int]) -> int that returns the distance between the first and second occurrence of the number 7 in the list nums.
You may assume that there will always be at least two occurrences of the number 7 in the list.
'''

# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

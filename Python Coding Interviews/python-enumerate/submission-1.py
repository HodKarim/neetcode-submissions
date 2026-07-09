from typing import List


def get_index_of_seven(nums: List[int]) -> int:
    #return index of first occurence of number 7 in list, or -1 if not in

    
    for i, num in enumerate(nums):
        if num == 7:
            return i
        else:
            continue
    return -1
        



def get_dist_between_sevens(nums: List[int]) -> int:
    #return distance between first n second occurence of number 7 in nums
    count = 0
    flag = 0
    for i, num in enumerate(nums):
        if flag == 1:
            count +=1

        if num == 7:
            if flag == 0:
                flag = 1
            else:
                break
    return count
'''
once we hit the first 7, start a count
count needs to keep going until another 7 is reached
'''
# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index_of_seven([2, 4, 7, 5, 7, 8, 4, 2]))

print(get_dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(get_dist_between_sevens([2, 7, 7, 7, 8]))
print(get_dist_between_sevens([7, 4, 8, 4, 2, 7]))

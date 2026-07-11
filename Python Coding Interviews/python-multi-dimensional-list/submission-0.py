from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    maxx = 0
    max_list = []
    for sublist in nested_arr:
        for element in sublist:
            if element > maxx:
                maxx = element
        max_list.append(maxx)
    return max_list


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))

'''
takes 2d list of ints and retrns list of maximum lements in each sublist
returned list much have the max elements from each sublist in the order they appear in the input list



'''
from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    '''
    takes list of integers arr and integer k
    convert list into deque
    rotate values in list to the right by k and return resulting deque

    so basically [1,2,3,4,5] ---> deque
    appendleft the end k times?
    '''

    queue = deque(arr)
    for i in range(k):
        queue.appendleft(queue.pop())
    return queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))

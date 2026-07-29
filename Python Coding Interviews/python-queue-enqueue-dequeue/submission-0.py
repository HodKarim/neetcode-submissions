from typing import List, Deque
from collections import deque


def rotate_list(arr: List[int], k: int) -> Deque[int]:
    '''
    takes list of integers arr and int k 
    convert list to dequeue
    then rotate values in list to the left by k steps and return resulting dequeue

    so a queue is fifo: first in are first out

    [1,2,3,4,5] 
    '''
    queue = deque(arr)
    for i in range(k):
        queue.append(queue.popleft())
    return queue



# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))


'''
queues enqueue and dequeue

python gives dequeue class from collections module that can be used for queue
'''

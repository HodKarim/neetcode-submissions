from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_list = []
    while len(arr) > 0:
        new_list.append(arr.pop())
    return new_list


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))


'''
append to push shit into stack
pop to remove and return top element in stack
stack is LIFO - last in first out
stack = [1,2]
stack.pop() # gives #2
stack.append(3) #gives [1,3]
stacl[-1] returns top element in stack

implement this function: reverse_list takes list of ints and returns new list in reverse order
'''
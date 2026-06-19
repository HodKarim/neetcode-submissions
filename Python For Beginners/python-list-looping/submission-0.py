from typing import List # used to add type hint for List

#accepts list of integers num and integer x
# return # of times x appears in list nums
def count_x(nums: List[int], x: int) -> int:

    count = 0
    for element in nums:
        if element == x:
            count += 1
    return count



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))

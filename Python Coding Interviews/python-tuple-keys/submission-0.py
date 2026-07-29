from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    '''
    takes 2d grid of ints and returns a set of tuples 
    where each tuple is a pair of row and column
    set should only have coordinates of cells w value of one

    traverse thru the list of lists and see which elems are 1. if 1, add row # and column # to set.
    '''

    sett = set()

    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[j][i]:
                sett.add((j, i))
    return sett


# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))

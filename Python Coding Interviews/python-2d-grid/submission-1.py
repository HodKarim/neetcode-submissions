from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    '''
    takes 2d grid and two ints r and c where r is index of row and c is index of column
    return true if cell at row r and col c is in bound of grid, false otherwise
    row = len(grid)
    col = len(grid[0])
    '''
    if r < len(grid) and c < len(grid[0]):
        return True
    else:
        return False




# do not modify below this line
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))

from typing import List


def in_bounds(grid: List[List[int]], r: int, c: int) -> bool:
    row_length = len(grid)
    column_length = len(grid[0])

    if r < row_length and c <column_length:
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

'''
implement function that takes a 2d grid and 2 integers r and c
r = index of a row
c = index of a column.
return true if cell at row r and comulm c is within bounds of grid, and false otherwise


laymans terms:
r > len(grid)
c > len(grid[0])
'''
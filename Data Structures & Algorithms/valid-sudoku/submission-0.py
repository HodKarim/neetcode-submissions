class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                value = board[r][c]

                #skip the empty cells (just use continue)
                if value == ".":
                    continue

                box = (r // 3, c // 3)

                rows.setdefault(r, set())
                cols.setdefault(c, set())
                boxes.setdefault(box, set())

                #duplicate found :/
                if (value in rows[r] or
                    value in cols[c] or
                    value in boxes[box]):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True


'''
Logic:
go thru alllllllll cell in the board
skip empty cells (".")
for each number, check three things: has it appeared in this row before, has it appeared in
this column before, has it appeared in this 3x3 box before

if any check is true return F
else add number to the row column n box sets
if finish scanning the board without duplicates return T

Pattern:
Hash Maps + Sets

Time Complexity:
O(1) because the board is 9x9 = 81 (O(81 is basically O(1)))

Space Complexity:
O(81) = O(1)
at most we store each cell once across the row, column, n box sets

Time to complete problem:
41 minutes 2 seconds (the problem itself took 30 minutes to logic through but i had to watch a vid 
on how to play sudoku to solve this)
'''
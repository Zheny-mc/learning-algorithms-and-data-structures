from leetcode.array.utils import *


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        R_cells = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == "R":
                    R_cells.append((y, x))
        count = 0
        # for y, x in R_cells:
            # вверх
            # вниз
            # влево
            # вправо
            # for c_j in range(x+1, m):


        return count


create_test(
    Solution().numRookCaptures,
[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]],
3
)

create_test(
    Solution().numRookCaptures,
[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]],
0
)

create_test(
    Solution().numRookCaptures,
[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]],
3
)

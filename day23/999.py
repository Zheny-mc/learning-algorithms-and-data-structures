from leetcode.array.utils import *


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        rook_cells = ( (y, x) for x in range(len(board[0])) for y in range(len(board)) if board[y][x] == "R" )

        is_pawn = lambda y, x: board[y][x] == "p"
        is_elephant = lambda y, x: board[y][x] == "B"

        count = 0
        for y, x in rook_cells:
            # вверх
            for c_y in range(y-1, 0-1, -1):
                if is_elephant(c_y, x):
                    break
                if is_pawn(c_y, x):
                    count += 1
                    break
            # вниз
            for c_y in range(y+1, n):
                if is_elephant(c_y, x):
                    break
                if is_pawn(c_y, x):
                    count += 1
                    break
            # влево
            for c_x in range(x-1, 0-1, -1):
                if is_elephant(y, c_x):
                    break
                if is_pawn(y, c_x):
                    count += 1
                    break
            # вправо
            for c_x in range(x+1, m):
                if is_elephant(y, c_x):
                    break
                if is_pawn(y, c_x):
                    count += 1
                    break
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


create_test(
    Solution().numRookCaptures,
[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".","p","p",".",".",".","."],[".","p","p","R",".","p",".","p"],[".",".",".","p",".",".",".","."],[".",".",".",".",".","p",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]],
4
)
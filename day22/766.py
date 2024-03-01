from leetcode.array.utils import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        base_cells = [(0, j) for j in range(len(matrix[0]))]
        base_cells.extend( ( (i, 0) for i in range(1, len(matrix))) )

        check_coord = lambda x, max_len: x >= 0 and x < (max_len-1)
        check_cell = lambda i, j: check_coord(i, len(matrix)) and check_coord(j, len(matrix[0]))

        for i, j in base_cells:
            c_i, c_j = i, j
            while check_cell(c_i, c_j):
                if matrix[c_i][c_j] != matrix[c_i+1][c_j+1]:
                    return False
                c_i, c_j = c_i+1, c_j+1
        return True

create_test(
    Solution().isToeplitzMatrix,
[[1,2,3,4],[5,1,2,3],[9,5,1,2]],
True
)

create_test(
    Solution().isToeplitzMatrix,
[[1,2],[2,2]],
False
)
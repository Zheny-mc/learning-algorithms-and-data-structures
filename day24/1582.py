from leetcode.array.utils import *


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sum_row = {i: sum(row) for i, row in enumerate(mat) }
        sum_col = {j: sum(col) for j, col in enumerate(zip(*mat)) }

        res = 0
        for i, i_v in sum_row.items():
            for j, j_v in sum_col.items():
                if mat[i][j] and i_v == 1 and j_v == 1:
                    res += 1
        return res



# create_test(
#     Solution().numSpecial,
# [[1,0,0],[0,0,1],[1,0,0]],
#     1
# )
#
# create_test(
#     Solution().numSpecial,
# [[1,0,0],[0,1,0],[0,0,1]],
# 3
# )

create_test(
    Solution().numSpecial,
[[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]],
1
)
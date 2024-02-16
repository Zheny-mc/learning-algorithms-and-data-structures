from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t_matrix = [[0 for _ in range(len(matrix)) ] for _ in range(len(matrix[0]))]
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                t_matrix[j][i] = matrix[i][j]
        return t_matrix



create_test(
    Solution().transpose,
[[1,2,3],[4,5,6],[7,8,9]],
[[1,4,7],[2,5,8],[3,6,9]]
)

create_test(
    Solution().transpose,
[[1,2,3],[4,5,6]],
[[1,4],[2,5],[3,6]]
)
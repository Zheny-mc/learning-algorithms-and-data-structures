from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_val_set = set((min(row) for row in matrix))
        for j in range(len(matrix[0])):
            max_val = -10**9
            for i in range(len(matrix)):
                max_val = max(max_val, matrix[i][j])

            if max_val in min_val_set:
                return [max_val]

        return []
            


create_test(
    Solution().luckyNumbers,
[[3,7,8],[9,11,13],[15,16,17]],
[15]
)

create_test(
    Solution().luckyNumbers,
[[1,10,4,2],[9,3,8,7],[15,16,17,12]],
[12]
)

create_test(
    Solution().luckyNumbers,
[[7,8],[1,2]],
[7]
)
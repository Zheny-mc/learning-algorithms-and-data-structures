from typing import List

def create_test(func, in_data, out_data):
    res = func(*in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        h = []
        get_s = lambda r, c: abs(r - rCenter) + abs(c - cCenter)
        for i in range(rows):
            for j in range(cols):
                h.append(([i, j], get_s(i, j)))
        h.sort(key=lambda x: x[1])
        return [coord for coord, val in h]


create_test(
    Solution().allCellsDistOrder,
    (1, 2, 0, 0),
    [[0,0],[0,1]]
)

create_test(
    Solution().allCellsDistOrder,
    (2, 3, 1, 2),
    [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
)
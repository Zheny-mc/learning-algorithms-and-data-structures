from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        check_coord = lambda x, n: x >= 0 and x < n
        check_cell = lambda y, x: check_coord(y, len(grid)) and check_coord(x, len(grid[0])) and grid[y][x] == 1

        perimetr = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    k = 0
                    # вверх
                    if check_cell(y - 1, x): k += 1
                    # вниз
                    if check_cell(y + 1, x): k += 1
                    # вправо
                    if check_cell(y, x + 1): k += 1
                    # влево
                    if check_cell(y, x - 1): k += 1
                    perimetr += 4 - k

        return perimetr


create_test(
    Solution().islandPerimeter,
[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],
16
)

create_test(
    Solution().islandPerimeter,
[[1]],
4
)

create_test(
    Solution().islandPerimeter,
[[1,0]],
4
)



from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            if sum(grid[i]) == n-1:
                return i
        return -1

res = Solution().findChampion([[0,1],[0,0]])
print(f'res = [{res}], answer = {res == 0}')

res = Solution().findChampion([[0,0,1],[1,0,1],[0,0,0]])
print(f'res = [{res}], answer = {res == 1}')
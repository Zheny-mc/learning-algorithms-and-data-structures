from utils import *

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        total = len(grid) * len(grid[0])
        k %= total

        if total == k:
            return grid

        q = Deque()
        count_append = total - k
        count_popleft = k
        def first_step(count_append):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if count_append <= 0:
                        return
                    q.append(grid[i][j])
                    count_append -= 1
        first_step(count_append)

        def second_step(count_popleft):
            for i in range(len(grid)-1, 0-1, -1):
                for j in range(len(grid[0])-1, 0-1, -1):
                    if count_popleft <= 0:
                        return
                    q.appendleft(grid[i][j])
                    count_popleft -= 1

        second_step(count_popleft)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = q.popleft()

        return grid
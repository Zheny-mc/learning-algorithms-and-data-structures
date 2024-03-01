from leetcode.array.utils import *


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = 10**9
        min_index = -1
        get_distance = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i, p in enumerate(points):
            c_x, c_y = p
            if c_x == x or c_y == y:
                if c_x == x and c_y == y:
                    return i

                distance = get_distance(p, (x, y))
                if min_distance > distance:
                    min_distance = distance
                    min_index = i

        return min_index


create_test(
    Solution().nearestValidPoint,
    (3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]),
    2
)

create_test(
    Solution().nearestValidPoint,
    (3, 4, [[3,4]]),
    2
)

create_test(
    Solution().nearestValidPoint,
    (3, 4, [[2,3]]),
    -1
)
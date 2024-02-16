from leetcode.array.utils import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0

        g.sort()
        s.sort()
        slow, fast = 0, 0

        while slow < len(g):
            res_find = None
            while fast < len(s):
                if s[fast] >= g[slow]:
                    res_find = fast
                    break
                fast += 1

            if res_find is None:
                return count
            else:
                count += 1
                fast += 1

            slow += 1

        return count

create_test(
    Solution().findContentChildren,
([1,2,3], [1,1]),
1
)

create_test(
    Solution().findContentChildren,
([1,2], [1,2,3]),
2
)


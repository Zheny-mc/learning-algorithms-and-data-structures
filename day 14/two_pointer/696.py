from leetcode.array.utils import *


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        i = 1
        prev, curr = 0, 1

        while i < len(s):
            if s[i-1] != s[i]:
                count += min(prev, curr)
                prev = curr
                curr = 1
            else:
                curr += 1

            i += 1

        count += min(prev, curr)
        return count



create_test(
    Solution().countBinarySubstrings,
"00110011",
    6
)

create_test(
    Solution().countBinarySubstrings,
"10101",
    4
)
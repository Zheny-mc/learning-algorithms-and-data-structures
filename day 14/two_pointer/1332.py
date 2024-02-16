from leetcode.array.utils import *


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0

        res = 1
        i, j = 0, len(s)-1
        while j > i:
            if s[i] != s[j]:
                res = 2
                break
            j -= 1
            i += 1
        return res

create_test(
    Solution().removePalindromeSub,
"ababa",
    1
)

create_test(
    Solution().removePalindromeSub,
"abb",
    2
)

create_test(
    Solution().removePalindromeSub,
"baabb",
    2
)
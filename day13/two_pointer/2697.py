from leetcode.array.utils import create_test


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = ''.join( (min(f, s) for f, s in zip(s[::-1], s)) )

        return res

create_test(
    Solution().makeSmallestPalindrome,
"egcfe",
"efcfe"
)

create_test(
    Solution().makeSmallestPalindrome,
"abcd",
"abba"
)

create_test(
    Solution().makeSmallestPalindrome,
"seven",
"neven"
)

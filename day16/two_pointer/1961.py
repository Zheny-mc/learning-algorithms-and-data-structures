from leetcode.array.utils import *

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res_s = ""
        for w in words:
            if s.startswith(res_s + w):
                res_s += w
            else:
                break
        return res_s == s


create_test(
    Solution().isPrefixString,
    ("iloveleetcode", ["i","love","leetcode","apples"]),
    True
)

create_test(
    Solution().isPrefixString,
    ("iloveleetcode", ["apples","i","love","leetcode"]),
    False
)
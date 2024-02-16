from leetcode.array.utils import *


class Solution:
    def reverseVowels(self, s: str) -> str:
        set_chars = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left, right = 0, len(s) - 1

        res_s = list(s)
        while left < right:
            if res_s[left] in set_chars and res_s[right] in set_chars:
                res_s[left], res_s[right] = res_s[right], res_s[left]
                left += 1
                right -= 1
            elif res_s[left] not in set_chars:
                left += 1
            elif res_s[right] not in set_chars:
                right -= 1

        return ''.join(res_s)

create_test(
    Solution().reverseVowels,
"hello",
"holle"
)

create_test(
    Solution().reverseVowels,
"leetcode",
"leotcede"
)


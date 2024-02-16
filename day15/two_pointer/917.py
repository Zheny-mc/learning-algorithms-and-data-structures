from leetcode.array.utils import *

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res = ['_'] * len(s)
        left, right = 0, len(s) - 1

        filter_eng = lambda x: (x >= ord('a') and x <= ord('z')) or (x >= ord('A') and x <= ord('Z'))

        while left <= right:
            is_left = filter_eng(ord(s[left]))
            is_right = filter_eng(ord(s[right]))

            if is_left and is_right:
                res[left], res[right] = s[right], s[left]
                left += 1
                right -= 1
            elif not is_left:
                res[left] = s[left]
                left += 1
            elif not is_right:
                res[right] = s[right]
                right -= 1

        return ''.join(res)

create_test(
    Solution().reverseOnlyLetters,
"ab-cd",
"dc-ba"
)

create_test(
    Solution().reverseOnlyLetters,
"a-bC-dEf-ghIj",
"j-Ih-gfE-dCba"
)

create_test(
    Solution().reverseOnlyLetters,
"Test1ng-Leet=code-Q!",
"Qedo1ct-eeLg=ntse-T!"
)
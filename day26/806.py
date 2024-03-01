from leetcode.array.utils import *


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        get_val = lambda c: widths[ord(c) % ord('a')]
        count_str = 0
        sum_val = 0
        for ch in s:
            if sum_val + get_val(ch) > 100:
                count_str += 1
                sum_val = 0
            sum_val += get_val(ch)

        if sum_val > 0:
            count_str += 1
        return [count_str, sum_val]


create_test(
    Solution().numberOfLines,
    ([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
            "abcdefghijklmnopqrstuvwxyz"),
    ([3,60])
)

create_test(
    Solution().numberOfLines,
    ([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
            "bbbcccdddaaa"),
    ([2,4])
)


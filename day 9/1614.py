
def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')


class Solution:
    def maxDepth(self, s: str) -> int:
        parenth = {
            '(': 1,
            ')': -1
        }

        max_count_parenth = 0
        pre_sum = 0
        for ch in s:
            if ch in parenth:
                pre_sum += parenth[ch]
                max_count_parenth = max(max_count_parenth, pre_sum)

        return max_count_parenth

create_test(
    Solution().maxDepth,
"(1+(2*3)+((8)/4))+1",
    3
)

create_test(
    Solution().maxDepth,
"(1)+((2))+(((3)))",
    3
)
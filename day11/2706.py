from typing import List

def create_test(func, in_data, out_data):
    res = func(*in_data)
    print(f'res = [{res}], answer = {res == out_data}')


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min_s = prices[0] + prices[1]
        if min_s > money:
            return money
        return money - min_s


create_test(
    Solution().buyChoco,
    ([1,2,2], 3),
    0
)

create_test(
    Solution().buyChoco,
    ([3,2,3], 3),
    3
)
create_test(
    Solution().buyChoco,
    ([98,54,6,34,66,63,52,39], 62),
    22
)
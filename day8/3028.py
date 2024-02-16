from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        pre_sum = 0
        count = 0
        for val in nums:
            pre_sum += val
            if pre_sum == 0:
                count += 1
        return count

create_test(
    Solution().returnToBoundaryCount,
    [2,3,-5],
    1
)

create_test(
    Solution().returnToBoundaryCount,
    [3,2,-3,-4],
    0
)




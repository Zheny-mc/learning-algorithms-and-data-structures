from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        add_sum = 0
        i = 0
        j = len(nums) - 1

        while j - i >= 1:
            concat_num = int(str(nums[i]) + str(nums[j]))
            add_sum += concat_num
            j -= 1
            i += 1

        if i == j:
            add_sum += nums[i]

        return add_sum


create_test(
    Solution().findTheArrayConcVal,
[7,52,2,4],
596
)

create_test(
    Solution().findTheArrayConcVal,
[5,14,13,8,12],
673
)
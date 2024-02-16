from typing import List, Tuple

def create_test(func, in_data, out_data):
    res = func(*in_data) if isinstance(in_data, Tuple) else func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:

    """
    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] < target:
                res += 1
    return res
    """
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        count = 0
        while right > left:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count



create_test(
    Solution().countPairs,
([-1,1,2,3,1], 2),
3
)

create_test(
    Solution().countPairs,
    ([-6,2,5,-2,-7,-1,3], -2),
    10
)

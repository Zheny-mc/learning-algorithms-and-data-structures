from leetcode.array.utils import *

class Solution:

    """
    max_num = -10**9
    for i in nums:
        ind = nums.count(-i)
        if ind > 0:
            max_num = max(max_num, i)

    return -1 if max_num == -10**9 else max_num
    """

    def findMaxK(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        left, right = 0, len(nums)-1
        while left < right:
            if -nums[left] == nums[right]:
                return nums[right]
            elif -nums[left] < nums[right]:
                right -= 1
            else:
                left += 1

        return -1




create_test(
    Solution().findMaxK,
[-1,2,-3,3],
3
)

create_test(
    Solution().findMaxK,
[-1,10,6,7,-7,1],
7
)

create_test(
    Solution().findMaxK,
[-10,8,6,7,-2,-3],
    -1
)
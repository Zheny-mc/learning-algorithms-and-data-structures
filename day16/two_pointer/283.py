from leetcode.array.utils import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_ind_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_ind_zero] = nums[i]
                last_ind_zero += 1

        for i in range(last_ind_zero, len(nums)):
            nums[i] = 0
        return nums

# create_test(
#     Solution().moveZeroes,
# [1, 2, 3],
# [1, 2, 3]
# )

create_test(
    Solution().moveZeroes,
[0,1,0,3,12],
[1,3,12,0,0]
)

# create_test(
#     Solution().moveZeroes,
# [0],
# [0]
# )
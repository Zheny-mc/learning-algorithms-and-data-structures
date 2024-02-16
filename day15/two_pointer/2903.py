from leetcode.array.utils import *


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if indexDifference == 0 and valueDifference == 0:
            return [0, 0]
        res = [-1, -1]

        for left in range(len(nums)):
            right = left + indexDifference
            if right >= len(nums):
                return [-1, -1]
            while right < len(nums):
                if abs(nums[left] - nums[right]) >= valueDifference:
                    return [left, right]
                right += 1
        return res

# create_test(
#     Solution().findIndices,
#     ([5,10], 1, 2),
#     [0,1]
# )     

create_test(
    Solution().findIndices,
    ([5,1,4,1], 2, 4),
    [0,3]
)

create_test(
    Solution().findIndices,
    ([2,1], 0, 0),
    [0, 0]
)

create_test(
    Solution().findIndices,
    ([1,2,3], 2, 4),
    [-1, -1]
)

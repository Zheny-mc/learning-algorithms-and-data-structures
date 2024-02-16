from leetcode.array.utils import *


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        right = 0
        lst_ind = []
        N = len(nums)
        for left in range(len(nums)):
            if nums[left] == key:
                while right <= left+k:
                    if abs(right - left) <= k and right < N:
                        lst_ind.append(right)
                    right += 1
        lst_ind.sort()
        return lst_ind

create_test(
    Solution().findKDistantIndices,
([3,4,9,1,3,9,5], 9, 1),
[1,2,3,4,5,6]
)

create_test(
    Solution().findKDistantIndices,
([2,2,2,2,2], 2, 2),
[0,1,2,3,4]
)

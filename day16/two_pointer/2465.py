from leetcode.array.utils import *

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1

        avg = lambda x, y: (x + y) / 2

        set_avg = set()
        while left < right:
            set_avg.add(avg(nums[left], nums[right]))

            left += 1
            right -= 1

        return len(set_avg)
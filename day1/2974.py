from typing import List


def numberGame(nums: List[int]) -> List[int]:
    nums.sort()
    for i in range(1, len(nums), 2):
        nums[i], nums[i - 1] = nums[i - 1], nums[i]
    return nums

res = numberGame(nums = [5,4,2,3])
# res = numberGame(nums = [2,5])
print(res)
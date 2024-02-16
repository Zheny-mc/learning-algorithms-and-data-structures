from typing import List, Optional


def create_test(func, in_data, out_data):
    res = func(*in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) <= 0:
            return None

        middle = len(nums) // 2

        return TreeNode(
            nums[middle],
            self.sortedArrayToBST(nums[:middle]),
            self.sortedArrayToBST(nums[middle + 1:])
        )

create_test(
    Solution().sortedArrayToBST,
    ([-10,-3,0,5,9]),
[0,-3,9,-10,None,5]
)

create_test(
    Solution().sortedArrayToBST,
    ([1,3]),
[3,1]
)
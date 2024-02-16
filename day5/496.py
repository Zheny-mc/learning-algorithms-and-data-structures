from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dct_nums = {val: i for i, val in enumerate(nums1)}

        ans = [0] * len(nums1)
        stack = []

        for i in range(len(nums2)-1, -1, -1):
            # print(stack[-1] if len(stack) > 0 else -1)
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if nums2[i] in dct_nums:
                if len(stack) == 0:
                    ans[dct_nums[nums2[i]]] = -1
                else:
                    ans[dct_nums[nums2[i]]] = stack[-1]

            stack.append(nums2[i])
        return ans





res = Solution().nextGreaterElement([4,1,2], [2,1,3,4])
print(f'res = [{res}], answer = {res == [-1, 3, 3]}')

# res = Solution().nextGreaterElement([2,4], [1,2,3,4])
# print(f'res = [{res}], answer = {res == [3,-1]}')
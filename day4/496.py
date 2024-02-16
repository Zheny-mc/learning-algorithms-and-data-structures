from typing import List


class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def processing(elem):
            ind = nums2.index(elem)
            for k in range(ind+1, len(nums2)):
                if nums2[k] > nums2[ind]:
                    return nums2[k]
            return -1

        return [processing(nums1[i]) for i in range(len(nums1))]



res = Solution().nextGreaterElement([4,1,2], [1,3,4,2])
print(f'res = [{res}], answer = {res == [-1,3,-1]}')

res = Solution().nextGreaterElement([2,4], [1,2,3,4])
print(f'res = [{res}], answer = {res == [3,-1]}')
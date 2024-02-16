from typing import List

def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
    res = [0] * 2
    n1, n2 = set(nums1), set(nums2)
    for i in nums1:
        if i in n2:
            res[0] += 1

    for i in nums2:
        if i in n1:
            res[1] += 1

    return res

print(findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]))
print(findIntersectionValues(nums1 = [3,4,2,3], nums2 = [1,5]))
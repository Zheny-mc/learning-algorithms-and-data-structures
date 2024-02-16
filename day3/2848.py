from typing import List

def numberOfPoints(nums: List[List[int]]) -> int:
    right = 0
    res = 0
    nums.sort(key=lambda x: x[0])
    for s, e in nums:
        if e <= right: continue
        if s > right:
            res += e - s + 1
            right = e
        else:
            res += e - right
            right = e
    return res




print(numberOfPoints([[300,600],[100,500],[400,700]]))
print(numberOfPoints([[1,3],[5,8]]) == 7)
from leetcode.array.utils import *


class Solution:

    def insert(self, arr, i, j):
        if j < len(arr):
            arr[j] = arr[i]
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count_zero = len([i for i in arr if i == 0])

        i, j = len(arr)-1, len(arr)+count_zero-1

        while i != j:
            self.insert(arr, i, j); j -= 1
            if arr[i] == 0:
                self.insert(arr, i, j); j -= 1
            i -= 1

        return arr


create_test(
    Solution().duplicateZeros,
[1,0,2,3,0,4,5,0],
[1,0,0,2,3,0,0,4]
)

create_test(
    Solution().duplicateZeros,
[1,2,3],
[1,2,3]
)
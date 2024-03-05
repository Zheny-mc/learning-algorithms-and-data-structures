import math

from utils import *

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        len_delete = ceil(len(arr) * 5 / 100)
        mean_val = round(sum(arr[i] for i in range(len_delete, len(arr)-len_delete)) / (len(arr) - 2*len_delete), 5)
        return mean_val

create_test(
    Solution().trimMean,
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3],
2.00000
)

create_test(
    Solution().trimMean,
[6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0],
4.00000
)

create_test(
    Solution().trimMean,
[6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4],
4.77778
)
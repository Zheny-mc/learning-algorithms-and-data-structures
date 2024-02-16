from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dct_pair = []
        j = 0
        min_diff = 10 ** 9
        while j < len(arr) - 1:
            diff = arr[j + 1] - arr[j]
            if min_diff > diff:
                min_diff = diff
            dct_pair.append(((arr[j], arr[j + 1]), diff))
            j += 1

        res = [k for k, v in dct_pair if v == min_diff]
        return res


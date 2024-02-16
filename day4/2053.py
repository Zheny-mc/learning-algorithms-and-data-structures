from typing import List
from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dct = Counter(arr)
        for s in arr:
            if dct[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""

res = Solution().kthDistinct(arr = ["d", "b","c", "b","c","a"], k = 2 )
print(f'res = [{res}], answer = {res == "a"}')

res = Solution().kthDistinct(arr = ["aaa", "aa", "a"], k = 1 )
print(f'res = [{res}], answer = {res == "aaa"}')

res = Solution().kthDistinct(arr = ["a","b","a"], k = 3 )
print(f'res = [{res}], answer = {res == ""}')


from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dct = Counter(nums)
        values = dct.values()
        max_freq = max(values)
        return sum((v for v in values if v == max_freq))





res = Solution().maxFrequencyElements([1,2,2,3,1,4])
print(f'res = [{res}], answer = {res == 4}')

res = Solution().maxFrequencyElements([1,2,3,4,5])
print(f'res = [{res}], answer = {res == 5}')
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = len(list(filter(lambda x: x % 2 == 0, position)))
        odd = len(position) - even

        if even == len(position) or odd == len(position):
            return 0

        return min(even, odd)

res = Solution().minCostToMoveChips([1,2,3])
print(f'res = [{res}], answer = {res == 1}')

res = Solution().minCostToMoveChips([2,2,2,3,3])
print(f'res = [{res}], answer = {res == 2}')

res = Solution().minCostToMoveChips([1,1000000000])
print(f'res = [{res}], answer = {res == 1}')
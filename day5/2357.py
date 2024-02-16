from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        current = 0
        for x in nums:
            x -= current
            if x > 0:
                current += x
                count += 1
        return count

res = Solution().minimumOperations([1,5,0,3,5])
print(f'res = [{res}], answer = {res == 3}')

res = Solution().minimumOperations([0])
print(f'res = [{res}], answer = {res == 0}')

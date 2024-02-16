from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count = {}
        for i in position:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        max_key = None
        max_val = 0
        for k, v in count.items():
            if v > max_val:
                max_val = v
                max_key = k
        gen_sum = 0
        res = 0
        for k, v in count.items():
            if k != max_key:
                for i in range(gen_sum, gen_sum+v):
                    res += i
                    count[max_key] += i
                gen_sum += v

        return res


res = Solution().minCostToMoveChips([1,2,3])
print(f'res = [{res}], answer = {res == 1}')

res = Solution().minCostToMoveChips([2,2,2,3,3])
print(f'res = [{res}], answer = {res == 2}')

res = Solution().minCostToMoveChips([1,1000000000])
print(f'res = [{res}], answer = {res == 1}')
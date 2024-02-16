from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frec_nums = {}
        for i in nums:
            if i not in frec_nums:
                frec_nums[i] = 1
            else:
                frec_nums[i] += 1

        lst = list(frec_nums.items())
        lst.sort(key=lambda x: x[0], reverse=True)
        lst.sort(key=lambda x: x[1])

        res = []
        for k, v in lst:
            res += [k for _ in range(v)]
        return res

create_test(
    Solution().frequencySort,
[1,1,2,2,2,3],
[3,1,1,2,2,2]
)

create_test(
    Solution().frequencySort,
[2,3,1,3,2],
[1,3,3,2,2]
)

create_test(
    Solution().frequencySort,
[-1,1,-6,4,5,-6,1,4,1],
[5,-1,4,4,-6,-6,1,1,1]
)
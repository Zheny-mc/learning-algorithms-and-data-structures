from typing import List

def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] != nums[j] and \
                        nums[j] != nums[k] and \
                        nums[k] != nums[i]:
                        count += 1
        return count

create_test(
    Solution().unequalTriplets,
[4,4,2,4,3],
3
)

create_test(
    Solution().unequalTriplets,
[1,1,1,1,1],
0
)


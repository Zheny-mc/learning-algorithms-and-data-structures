from typing import List

def findKOr(nums: List[int], k: int) -> int:
    answer = 0
    for i in range(31+1):
        count = 0
        for j_num in range(len(nums)):
            if nums[j_num] >> i & 1:
                count += 1

        if count >= k:
            answer += (1 << i)

    return answer

res = findKOr(nums = [7,12,9,8,9,15], k = 4)
print(f'1)res={res}, {res == 9}')

res = findKOr(nums = [2,12,1,11,4,5], k = 6)
print(f'2)res={res}, {res == 0}')

res = findKOr(nums = [10,8,5,9,11,6,8], k = 1)
print(f'3)res={res}, {res == 15}')

from typing import List, Dict


def sumCounts(nums: List[int]) -> int:
    summa = 0
    for i in range(len(nums)):
        check = set()
        for j in range(i, len(nums)):
            check.add(nums[j])
            summa += len(check)**2
    return summa

result = sumCounts(nums = [1,2,1])
print(result)
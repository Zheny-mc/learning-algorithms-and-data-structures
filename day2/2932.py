from typing import List

def maximumStrongPairXor(nums: List[int]) -> int:
    max_xor = -10**6
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                max_xor = max(max_xor, nums[i] ^ nums[j])
    return max_xor


print(maximumStrongPairXor([1,2,3,4,5]))
print(maximumStrongPairXor([10,100]))
print(maximumStrongPairXor([5,6,25,30]))

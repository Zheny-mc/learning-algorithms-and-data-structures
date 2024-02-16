from typing import List

def findPeaks(mountain: List[int]) -> List[int]:
    check_mount = lambda k: mountain[k] > mountain[k - 1] and mountain[k] > mountain[k + 1]
    res = (i for i in range(1, len(mountain)-1) if check_mount(i))
    return list(res)



res = findPeaks([2,4,2])
print(res)
res = findPeaks([1,4,3,8,5])
print(res)
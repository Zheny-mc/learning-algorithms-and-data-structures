from typing import List

def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
    set_nums = set()
    res = {'a': 0, 'b': 0}
    for i in range(len(grid)):
        for el in grid[i]:
            if el not in set_nums:
                set_nums.add(el)
            else:
                res['a'] = el

    max_elem = len(grid) ** 2
    res['b'] = sum(range(1, max_elem+1)) - sum(set_nums)
    return [res['a'], res['b']]



res = findMissingAndRepeatedValues([[1,3],[2,2]])
print(f'1)res={res}, {res == [2,4]}')

res = findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])
print(f'2)res={res}, {res == [9,5]}')
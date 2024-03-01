from leetcode.array.utils import *

def processing(lst1, lst2):
    res = list(set(lst1) & set(lst2))
    res.sort()
    return res

# in_data = (list(map(int, input().split())) for _ in range(2))
# print(*processing(*in_data))

create_test(
    processing,
([1, 3, 2], [4, 3, 2]),
(2, 3)
)

create_test(
    processing,
([1, 2, 6, 4, 5, 7], [10, 2, 3, 4, 8]),
(2, 4)
)
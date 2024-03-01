from leetcode.array.utils import *

processing = lambda in_data: len(set(map(int, in_data.split())))
# print(processing(input()))


create_test(
    processing,
'1 2 3 2 1',
3
)

create_test(
    processing,
'1 2 3 4 5 6 7 8 9 10',
10
)

create_test(
    processing,
'1 2 3 4 5 1 2 1 2 7 3',
6
)
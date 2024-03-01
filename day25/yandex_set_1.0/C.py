from leetcode.array.utils import *

def get_input():
    N, M = map(int, input().split())
    color_A = [int(input()) for _ in range(N)]
    color_B = [int(input()) for _ in range(M)]
    return (N, M, color_A, color_B)

def out_data(res):
    print(res[0])
    print(*res[1])
    print(res[2])
    print(*res[3])
    print(res[4])
    print(*res[5])

def processing(N, M, color_A, color_B):
    set_color_A = set(color_A)
    set_color_B = set(color_B)
    gen_colors = set_color_A & set_color_B
    other_color_A = list(set_color_A - gen_colors)
    other_color_A.sort()
    other_color_B = list(set_color_B - gen_colors)
    other_color_B.sort()

    return (len(gen_colors), sorted(gen_colors),
            len(other_color_A), other_color_A,
            len(other_color_B), other_color_B)

# in_data = get_input()
# out_data(processing(*in_data))

create_test(
    processing,
(4, 3, [0, 1, 10, 9], [1, 3, 0]),
(2, [0, 1], 2, [9, 10], 1, [3])
)

create_test(
    processing,
(2, 2, [1, 2], [2, 3]),
(1, [2], 1, [1], 1, [3])
)

create_test(
    processing,
(0, 0, [], []),
(0, [], 0, [], 0, [])
)



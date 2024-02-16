from typing import List

def create_test(func, in_data, out_data):
    res = func(*in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dct_chrs = {i: chr(i + ord('a')) for i in range(len(distance))}

        count_dct = {}
        for i, val in enumerate(s):
            if val in count_dct:
                count_dct[val] = i - count_dct[val] -1
            else:
                count_dct[val] = i

        for i, val in enumerate(distance):
            if dct_chrs[i] not in count_dct:
                continue
            elif val != count_dct[dct_chrs[i]]:
                return False

        return True



create_test(
    Solution().checkDistances,
    ("abaccb",
            [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    True
)

create_test(
    Solution().checkDistances,
("aa",
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]),
    False

)
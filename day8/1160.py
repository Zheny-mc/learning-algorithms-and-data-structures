from typing import List

def create_test(func, in_data, out_data):
    res = func(*in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:

    def countCharacters(self, words: List[str], chars: str) -> int:
        def counter(word):
            dct = {}
            for i in word:
                if i not in dct:
                    dct[i] = 1
                else:
                    dct[i] += 1
            return dct

        couter_chars = counter(chars[:])
        summa = 0
        for word in words:
            c_w = counter(word)
            flag = True
            for k, v in c_w.items():
                if not (k in couter_chars and couter_chars[k] >= v):
                    flag = False
                    break
            if flag:
                summa += len(word)

        return summa


create_test(
    Solution().countCharacters,
    (["cat","bt","hat","tree"],"atach"),
    6
)

create_test(
    Solution().countCharacters,
    (["hello","world","leetcode"], "welldonehoneyr"),
    10
)
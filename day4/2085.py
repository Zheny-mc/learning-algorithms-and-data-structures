from functools import reduce
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        gen_dct = {}
        for w in words1:
            if w not in gen_dct:
                gen_dct[w] = [1, 0]
            else:
                gen_dct[w][0] += 1

        for w in words2:
            if w in gen_dct:
                gen_dct[w][1] += 1

        return reduce(lambda x, y: x+y, ( 1 for w, count in gen_dct.items() if count == [1, 1] ), 0)


res = Solution().countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"])
print(f'res = [{res}], answer = {res == 2}')

res = Solution().countWords(["b","bb","bbb"], ["a","aa","aaa"])
print(f'res = [{res}], answer = {res == 0}')

res = Solution().countWords(["a","ab"], ["a","a","a","ab"])
print(f'res = [{res}], answer = {res == 1}')
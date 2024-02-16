from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ( set("qwertyuiopQWERTYUIOP"), set("asdfghjklASDFGHJKL"), set("zxcvbnmZXCVBNM") )

        res = []
        for word in words:
            set_word = set(word)
            k_rows = 0
            for i in range(len(rows)):
                if len(set_word & rows[i]) > 0:
                    k_rows += 1
            if k_rows == 1:
                res.append(word)
        return res

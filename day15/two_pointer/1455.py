from leetcode.array.utils import *

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        len_searchWord = len(searchWord)

        def processing_word(w, s_w):
            left, right = 0, len_searchWord - 1
            while left <= right:
                if w[left] != s_w[left] or w[right] != s_w[right]:
                    return False
                left += 1
                right -= 1
            return True

        for i, word in enumerate(words):
            if len(word) >= len_searchWord and processing_word(word, searchWord):
                return i+1

        return -1


create_test(
    Solution().isPrefixOfWord,
    ("i love eating burger", "burg"),
    4
)

create_test(
    Solution().isPrefixOfWord,
    ("this problem is an easy problem", "pro"),
    2
)

create_test(
    Solution().isPrefixOfWord,
    ("i am tired", "you"),
    -1
)
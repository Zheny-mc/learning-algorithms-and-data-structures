from leetcode.array.utils import *

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = Deque()
        stack_t = Deque()

        for i in s:
            if i.isalpha():
                stack_s.append(i)
            elif i == '#' and len(stack_s) > 0:
                stack_s.pop()

        for j in t:
            if j.isalpha():
                stack_t.append(j)
            elif j == '#' and len(stack_t) > 0:
                stack_t.pop()

        return tuple(stack_s) == tuple(stack_t)


# create_test(
#     Solution().backspaceCompare,
# ("ab#c", "ad#c"),
# True
# )
#
# create_test(
#     Solution().backspaceCompare,
# ("ab##", "c#d#"),
# True
# )

create_test(
    Solution().backspaceCompare,
("a#c", "b"),
False
)


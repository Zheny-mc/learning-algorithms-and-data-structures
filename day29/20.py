from utils import *

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {']': '[', ')': '(', '}': '{'}
        stack = Deque()
        for i in s:
            if i in close_to_open:
                if stack and stack[-1] == close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return len(stack) == 0


create_test(
    Solution().isValid,
"()",
True
)

create_test(
    Solution().isValid,
"()[]{}",
True
)

create_test(
    Solution().isValid,
"(]",
False
)



def create_test(func, in_data, out_data):
    res = func(in_data)
    print(f'res = [{res}], answer = {res == out_data}')

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        open_ = 0
        close_ = 0
        start = 0

        for i, ch in enumerate(s):
            if ch == '(':
                open_ += 1
            elif ch == ')':
                close_ += 1

            if open_ == close_:
                res.append(s[start+1: i])
                start = i + 1
                open_ = 0
                close_ = 0

        return ''.join(res)



create_test(
    Solution().removeOuterParentheses,
"(()())(())",
"()()()"
)

create_test(
    Solution().removeOuterParentheses,
"(()())(())(()(()))",
"()()()()(())"
)

create_test(
    Solution().removeOuterParentheses,
"()()",
""
)

create_test(
    Solution().removeOuterParentheses,
"((()())(()()))",
"(()())(()())"
)
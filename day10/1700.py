from typing import List
from collections import deque

def create_test(func, in_data, out_data):
    res = func(*in_data)
    print(f'res = [{res}], answer = {res == out_data}')


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        deque_stud = deque(students)  # очередь студентов
        sandwiches.reverse()  # стек бутербродов

        count_error = 0

        while deque_stud and len(deque_stud) != count_error:
            stud = deque_stud.popleft()
            if stud == sandwiches[-1]:
                sandwiches.pop()
                count_error = 0
                continue
            else:
                count_error += 1
                deque_stud.append(stud)

        return len(deque_stud)





create_test(
    Solution().countStudents,
    ([1,1,0,0], [0,1,0,1]),
    0
)


create_test(
    Solution().countStudents,
    ([1,1,1,0,0,1], [1,0,0,0,1,1]),
    3
)



# d = deque('ghi')                 # make a new deque with three items
# d.append('777')
# d.appendleft('888')
# d.pop()
# d.popleft()
# print(d.index('h'))
# d.insert(1, '555')
# print(d)
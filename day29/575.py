from utils import *

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len( set(candyType) ),
                   (len(candyType) // 2)
                )

create_test(
    Solution().distributeCandies,
[1,1,2,2,3,3],
3
)


create_test(
    Solution().distributeCandies,
[1,1,2,3],
2
)

create_test(
    Solution().distributeCandies,
[6,6,6,6],
1
)

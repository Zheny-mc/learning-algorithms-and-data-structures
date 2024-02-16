from leetcode.array.utils import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def getLen(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        len_a = getLen(headA)
        len_b = getLen(headB)

        while len_a > len_b:
            headA = headA.next
            len_a -= 1

        while len_b > len_a:
            headB = headB.next
            len_b -= 1

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        prev = dummy
        while l1 or l2 or carry == 1:
            total = 0
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            if carry:
                total += 1
                carry = 0
            if total >= 10:
                total -= 10
                carry = 1
            curr = ListNode(total, None)
            prev.next = curr
            prev = curr
        return dummy.next

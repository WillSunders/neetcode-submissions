# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        count = 1
        while count < n:
            right = right.next
            count += 1
        prev = None
        while right.next:
            prev = left
            left = left.next
            right = right.next
        if not prev:
            return head.next
        prev.next = left.next
        return head

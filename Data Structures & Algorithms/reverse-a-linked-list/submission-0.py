# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        prev = None
        while head:
            current = head
            head = current.next
            current.next = prev
            prev = current
            current = current.next
        return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1
        while curr.next:
            curr = curr.next
            count += 1
        loc = count - n
        curr = head
        prev = None
        while loc > 0:
            prev = curr
            curr = curr.next
            loc -= 1
        if not prev:
            if not head.next:
                return None
            return head.next
        prev.next = curr.next
        return head

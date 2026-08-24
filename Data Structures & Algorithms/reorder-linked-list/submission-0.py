# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        half = self.reverse(half)
        slow.next = None
        while head and half:
            temphead = head.next
            temphalf = half.next
            head.next = half
            half.next = temphead
            half = temphalf
            head = temphead
    def reverse(self, curr: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
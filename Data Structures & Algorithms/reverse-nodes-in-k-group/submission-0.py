# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        current = head
        prev = dummy
        count = 1
        while current:
            if count >= k:
                count = 1
                start, end, nextH = self.reverse(head, k)
                prev.next = start
                end.next = nextH
                prev = end
                head = nextH
                current = nextH
                continue
            current = current.next
            count += 1
        return dummy.next

    def reverse(self, head: ListNode, k: int) -> tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]:
        count = 0
        prev = None
        current = head
        temp = current.next
        while count < k and current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            count += 1
        return prev, head, temp
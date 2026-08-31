# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        newList = []
        for i in range(0, len(lists) - 1, 2):
            newList.append(self.merge2Lists(lists[i], lists[i+1]))
        if len(lists) % 2 == 1:
            newList.append(lists[-1])
        if len(newList) == 1:
            return newList[0]
        return self.mergeKLists(newList)

       

    def merge2Lists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while node1 or node2:
            if not node2:
                current.next = node1
                return dummy.next
            if not node1:
                current.next = node2
                return dummy.next
            if node1.val < node2.val:
                current.next = node1
                node1 = node1.next
            else:
                current.next = node2
                node2 = node2.next
            current = current.next
        return None
        
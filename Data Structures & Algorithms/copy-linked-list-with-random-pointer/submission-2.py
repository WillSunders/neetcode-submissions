"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        vals = {}
        curr = head
        while curr:
            newHead = Node(curr.val, None, None)
            vals[curr] = newHead
            curr = curr.next
        curr = head
        while curr:
            newHead = vals[curr]
            if curr.next:
                newHead.next = vals[curr.next]
            if curr.random:
                newHead.random = vals[curr.random]
            curr = curr.next
        return vals[head]
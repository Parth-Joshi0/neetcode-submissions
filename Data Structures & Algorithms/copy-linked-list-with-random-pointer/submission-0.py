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
        seen = {None : None}

        curr = head
        while curr:
            new = Node(curr.val)
            seen[curr] = new
            curr = curr.next

        curr = head
        while curr:
            new = seen[curr]
            new.next = seen[curr.next]
            new.random = seen[curr.random]
            curr = curr.next
        return seen[head]

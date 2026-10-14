# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None
        while fast:
            fast = fast.next
            slow = slow.next
            if not fast:
                return False
            fast = fast.next
            if fast == slow:
                return True
        return False
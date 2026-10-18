# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 0
        while curr.next:
            count += 1
            curr = curr.next
        
        node = count - n + 1
        curr = head
        prev = None
        while node != 0:
            prev = curr
            curr = curr.next
            node -= 1
        if curr == head:
            return curr.next
        
        prev.next = curr.next
        curr.next = None
        return head

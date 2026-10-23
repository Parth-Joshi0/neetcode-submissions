# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode(0)
        head = curr
        carry = 0
        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            add = l1.val + l2.val + carry
            if add >= 10:
                carry = 1
                add -= 10
            else:
                carry = 0
            curr.next = ListNode(add)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if carry:
            curr.next = ListNode(carry)

        return head.next
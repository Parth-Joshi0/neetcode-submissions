
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def reverseList(top: Optional[ListNode]) -> Optional[ListNode]:
            if not top:
                return

            prev = top
            curr = top.next
            prev.next = None

            while curr:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward

            return prev

        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        list2 = reverseList(slow.next)
        slow.next = None
        list1 = head

        while list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            list2.next = next1

            list1 = next1
            list2 = next2

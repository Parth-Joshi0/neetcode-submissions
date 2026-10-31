
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = head
        prev_tail = None

        while start:
            end = start

            # Find the node immediately after k nodes
            for i in range(k):
                if not end:
                    return head
                end = end.next

            # Reverse current group
            new_head = self.reverseList(start, end)

            # Connect previous group
            if prev_tail:
                prev_tail.next = new_head
            else:
                head = new_head

            # Original start is now the tail
            prev_tail = start
            start.next = end

            # Move to next group
            start = end

        return head

    def reverseList(self, head, end):
        prev = None
        curr = head

        while curr != end:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward

        return prev

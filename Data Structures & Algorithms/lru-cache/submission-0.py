
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}  # key -> LinkedListNode
        self.head = None
        self.back = None

    def get(self, key: int) -> int:
        Node = self.storage.get(key, None)
        if Node is None:
            return -1

        # Already most recently used
        if Node == self.back:
            return Node.val

        prev = Node.prev
        next = Node.next

        # Remove Node from its current position
        if prev:
            prev.next = next
        else:
            self.head = next

        if next:
            next.prev = prev

        # Move Node to the back
        self.back.next = Node
        Node.prev = self.back
        Node.next = None
        self.back = Node

        return Node.val

    def put(self, key: int, value: int) -> None:
        # Key already exists
        if key in self.storage:
            Node = self.storage[key]
            Node.val = value
            self.get(key)
            return

        # Cache is full
        if len(self.storage) == self.capacity:
            old = self.head
            del self.storage[old.key]

            self.head = old.next

            if self.head:
                self.head.prev = None
            else:
                self.back = None

        # Add new Node to the back
        Node = LinkedListNode(key, value, None, self.back)

        if self.back:
            self.back.next = Node
        else:
            self.head = Node

        self.back = Node
        self.storage[key] = Node


class LinkedListNode:

    def __init__(self, key, val, next, prev):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

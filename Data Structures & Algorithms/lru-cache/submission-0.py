class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hm = {}

    def moveToTail(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        node = self.hm[key]
        self.moveToTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self.moveToTail(node)
        else:
            if len(self.hm) == self.capacity:
                target = self.head.next
                self.head.next = target.next
                target.next.prev = self.head
                del self.hm[target.key]

            node = ListNode(key, value)
            self.hm[key] = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node

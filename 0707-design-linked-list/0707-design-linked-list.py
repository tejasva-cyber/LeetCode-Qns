class _Node(object):
    __slots__ = ('val', 'prev', 'next')

    def __init__(self, val=0, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node


class MyLinkedList(object):
    def __init__(self):
        self.size = 0
        # Dummy sentinels eliminate empty-list and boundary pointer checks
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _get_node(self, index):
        # Bidirectional traversal: start from the closer sentinel (max N/2 hops)
        if index < (self.size >> 1):
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
        return curr

    def _insert_between(self, val, prev_node, next_node):
        node = _Node(val, prev_node, next_node)
        prev_node.next = node
        next_node.prev = node
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        return self._get_node(index).val

    def addAtHead(self, val):
        self._insert_between(val, self.head, self.head.next)

    def addAtTail(self, val):
        self._insert_between(val, self.tail.prev, self.tail)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return

        succ = self._get_node(index)
        self._insert_between(val, succ.prev, succ)

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        node = self._get_node(index)
        # Safe-unlink invariant: verify neighbor symmetry before rewiring
        if node.prev.next is not node or node.next.prev is not node:
            raise RuntimeError("Corrupted doubly linked list pointers")

        node.prev.next = node.next
        node.next.prev = node.prev

        # Explicitly scrub detached pointers to prevent dangling references
        node.prev = None
        node.next = None
        self.size -= 1
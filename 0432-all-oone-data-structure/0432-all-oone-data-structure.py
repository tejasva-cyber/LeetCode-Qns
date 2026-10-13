class Node(object):
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):
    def __init__(self):
        # Hash map maps the string to its exact Node in the Doubly Linked List
        self.mapping = {}
        
        # Guard rails: Dummy head and tail nodes to eliminate edge-case pointer crashes
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.mapping:
            # 1. Payload is completely new
            if self.head.next.count != 1:
                self._insert_after(Node(1), self.head)
            self.head.next.keys.add(key)
            self.mapping[key] = self.head.next
        else:
            # 2. Payload exists, shift it to the next frequency bracket
            curr_node = self.mapping[key]
            nxt_count = curr_node.count + 1
            
            if curr_node.next.count != nxt_count:
                self._insert_after(Node(nxt_count), curr_node)
                
            curr_node.next.keys.add(key)
            self.mapping[key] = curr_node.next
            
            # Clean up the previous memory state
            curr_node.keys.remove(key)
            if not curr_node.keys:
                self._remove(curr_node)

    def dec(self, key):
        if key not in self.mapping:
            return
            
        curr_node = self.mapping[key]
        if curr_node.count == 1:
            # Payload drops to zero, completely unallocate
            del self.mapping[key]
        else:
            # Payload drops one frequency bracket
            prev_count = curr_node.count - 1
            if curr_node.prev.count != prev_count:
                self._insert_after(Node(prev_count), curr_node.prev)
                
            curr_node.prev.keys.add(key)
            self.mapping[key] = curr_node.prev
            
        # Clean up the previous memory state
        curr_node.keys.remove(key)
        if not curr_node.keys:
            self._remove(curr_node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        # Version-agnostic O(1) retrieval from a set
        for k in self.tail.prev.keys:
            return k

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        for k in self.head.next.keys:
            return k
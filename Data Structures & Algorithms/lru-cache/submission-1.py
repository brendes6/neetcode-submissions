"""
LRU cache: maintain a cache in a dictionary, but also store a 
linked list representing key access recency where the front is
the least recently used. Will need to have helper functions for 
directly removing nodes from a specific spot in the list, adding
to back, and retrieving + removing the val at front of linked list.

"""

class ListNode:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.nodeMap = {}
        self.dummyHead, self.dummyTail = ListNode(), ListNode()

    
    def add_to_back(self, node):
        if not self.dummyHead.nxt:
            self.dummyHead.nxt = node
            self.dummyTail.prev = node
            node.prev = self.dummyHead
            node.nxt = self.dummyTail
        else:
            tail = self.dummyTail.prev
            tail.nxt = node
            node.prev = tail
            node.nxt = self.dummyTail
            self.dummyTail.prev = node
    
    def remove_node(self, node):
        prev, nxt = node.prev, node.nxt
        if prev:
            prev.nxt = nxt
        if nxt:
            nxt.prev = prev
    
    def pop_front(self):
        node = self.dummyHead.nxt

        del self.cache[node.val]
        del self.nodeMap[node.val]

        self.dummyHead.nxt = node.nxt
        nxt = node.nxt
        if nxt:
            nxt.prev = self.dummyHead
        
        if self.dummyTail.prev == node:
            self.dummyTail.prev = None

    
    def use(self, key):
        # either get or create node

        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.remove_node(node)
        else:
            node = ListNode(val=key)
            self.nodeMap[key] = node
        
        self.add_to_back(node)


        
    
    def get(self, key: int) -> int:
        # print("getting", key)
        if key not in self.cache:
            return -1
        

        self.use(key)
        return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        # print("putting", key)
        if key not in self.cache:
            if self.capacity == len(self.cache):
                print("capacity reached, popping")
                self.pop_front()


        self.cache[key] = value


        self.use(key)

        

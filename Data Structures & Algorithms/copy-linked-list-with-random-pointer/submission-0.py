"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        clones = {}


        cur, prev = head, None

        while cur:

            new_node = Node(x=cur.val)
            clones[cur] = new_node

            if prev:
                prev.next = new_node
            
            cur, prev = cur.next, new_node
        
        cur2, ret = head, clones[head]

        while cur2:
            cop = clones[cur2]
            if cur2.random:
                cop.random = clones[cur2.random]
            
            cur2 = cur2.next
        
        return ret






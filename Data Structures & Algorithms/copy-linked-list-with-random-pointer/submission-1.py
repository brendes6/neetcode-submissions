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

        pass1 = head
        while pass1:
            new_node = Node(x=pass1.val)
            clones[pass1] = new_node
            pass1 = pass1.next


        cur, ret = head, clones[head]

        while cur:
            
            if cur.next:
                clones[cur].next = clones[cur.next]
            if cur.random:
                clones[cur].random = clones[cur.random]
            cur = cur.next
                
        
        return ret






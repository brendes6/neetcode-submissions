# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Strategy: store ListNode's in a list where we can have
        # 2 pointers to know leftmost and rightmost vals
        # iterate pointers to select correcet node per iteration
        # make dummy node, set dummy next to left val
        # set left next to right, increment l. Set right next to l,
        # increment r.
        # Strategy: store ListNode's in a list where we can have
        # 2 pointers to know leftmost and rightmost vals
        # iterate pointers to select correcet node per iteration
        # make dummy node, set dummy next to left val
        # set left next to right, increment l. Set right next to l,
        # increment r.
        if not head or not head.next:
            return None

        nodes = []

        # add nodes to list
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        l, r = 0, len(nodes)-1

        while l<r:
            nodes[l].next = nodes[r]
            l += 1
            if l==r:
                break

            nodes[r].next = nodes[l]
            r -= 1
        
        nodes[l].next = None
        

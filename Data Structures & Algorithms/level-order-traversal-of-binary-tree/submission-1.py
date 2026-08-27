# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Pretty basic: what we want to do is just run a leveled BFS where we store
a current level in a list, and iterate all nodes in the level adding them to
a next level.

e.g. starting with just root, we add roots children to a list, then all those
nodes children to a list, recurse
"""

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []


        # maintain 'next' layer list, and layer tracker

        levels = []
        cur, vals = [root], [root.val]

        while cur:
            new_level = []
            new_vals = []

            levels.append(vals)

            for node in cur:
                if node.left:
                    new_level.append(node.left)
                    new_vals.append(node.left.val)
                if node.right:
                    new_level.append(node.right)
                    new_vals.append(node.right.val)

            
            cur = new_level
            vals = new_vals
        
        return levels

        
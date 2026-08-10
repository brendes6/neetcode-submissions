# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """ strategy: since it is a binary search tree, its much easier. What we can do is
        iterate the tree, and there are two scenarios:
        1. both p and q are < current node.val -> mode left
        2. both p and q are > current node.val -> move right
        3. else, either p or q  .val == node.val -> this is lowest common ancestor

        """

        if not root or not p or not q:
            return None

        
        def dfs(node, p, q):
            if (p.val < node.val) and (q.val < node.val):
                return dfs(node.left, p, q)
            elif (p.val > node.val) and (q.val > node.val):
                return dfs(node.right, p, q)
            else:
                return node
        
        return dfs(root, p, q)
        
        


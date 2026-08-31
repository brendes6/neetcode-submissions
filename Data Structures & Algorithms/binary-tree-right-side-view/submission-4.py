# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # explore levels, tracking val of rightmost node
        if not root:
            return []
        

        levels = [[root]]
        vals = []

        while levels:
            level = levels.pop()
            new_level = []

            vals.append(level[-1].val)

            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            
            if not new_level:
                break

            levels.append(new_level)
        
        return vals
        
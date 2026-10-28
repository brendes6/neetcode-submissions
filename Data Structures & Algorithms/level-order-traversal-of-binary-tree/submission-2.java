/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        // appraoch: store current level in a list, add to new list
        // each time, and also iterate and make new list then replace

        if (root == null){
            return new ArrayList<>();
        }

        List<TreeNode> level = new ArrayList<>();
        level.add(root);

        List<List<Integer>> res = new ArrayList<>();

        while (level.size() > 0){

            List<TreeNode> new_level = new ArrayList<>();
            List<Integer> int_level = new ArrayList<>();

            for (TreeNode node : level){

                int_level.add(node.val);

                if (node.left != null){
                    new_level.add(node.left);
                }

                if (node.right != null){
                    new_level.add(node.right);
                }
            }

            res.add(int_level);

            if (new_level.size() == 0){
                return res;
            }
            
            level = new_level;
        }

        return res;
        
    }
}

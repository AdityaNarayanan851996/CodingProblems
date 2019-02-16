                      //Q) 701. Insert into a Binary Search Tree
                      // https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public void helper(TreeNode root,int val){
        if(root!= null){
            if(root.val > val){
                if(root.left ==null){
                    root.left = new TreeNode(val);
                }else{
                    helper(root.left,val);
                }
                
            }else{
                if(root.right ==null){
                    root.right = new TreeNode(val);

                }else{
                    helper(root.right,val);
                }
                
            }
        }

    }
    public TreeNode insertIntoBST(TreeNode root, int val) {
        
        
        TreeNode act_root = root;
        
        helper(root,val);
        
        return act_root;
        
        
    }
}

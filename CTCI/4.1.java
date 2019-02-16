// 			110. Balanced Binary Tree
// 			https://leetcode.com/problems/balanced-binary-tree/description/
//code
/**
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
    public int maxDepth(TreeNode root){
        if(root == null){
            return 0;
        }
        else{
            return 1 + Math.max(maxDepth(root.left),maxDepth(root.right));
        }
    
    }
    public boolean checker(TreeNode root){
        if(root == null){
            return true;
        }else{
            if(Math.abs(maxDepth(root.left) - maxDepth(root.right)) > 1 ){
                return false;
            }else{
                return true;
            }
        }
    }
    boolean flag = true;
    public boolean inOrder(TreeNode root){
        if(root!=null){
            if(checker(root) == false){
                flag = false;
                return flag;
            }else{
                inOrder(root.left);
                inOrder(root.right);
            }
        }
        return flag;
    }
    public boolean isBalanced(TreeNode root) {
        //System.out.println(maxDepth(root.right));
        return inOrder(root);
        
        
    }
}
//Q) https://leetcode.com/problems/subtree-of-another-tree/description/
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
    /*
    List<Integer> s  = new ArrayList<>();
    public void preOrder(TreeNode root){
        if(root!=null){
            s.add(root.val);
            preOrder(root.left);
            preOrder(root.right);
        }
    }
    public void inOrder(TreeNode root){
        if(root!=null){
            
            inOrder(root.left);
            s.add(root.val);
            inOrder(root.right);
        }
    }
    public void postOrder(TreeNode root){
        if(root!=null){
            
            postOrder(root.left);
            postOrder(root.right);
            s.add(root.val);
        }
    }
    */
    public boolean identical(TreeNode s,TreeNode t){
        if(s == null && t == null){
            return true;
        }
        if(s == null || t == null){
            return false;
        }
        if(s.val == t.val){
            if(identical(s.left,t.left) && identical(s.right,t.right)){
                return true;
            }
        }
        return false;
    }
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(t == null){
            return true;
        }
        if(s == null){
            return false;
        }
        if(identical(s,t)){
            return true;
        }
        
        return isSubtree(s.left,t) || isSubtree(s.right,t);
        
    }
}

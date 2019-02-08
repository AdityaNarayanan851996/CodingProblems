// 			Q) 297. Serialize and Deserialize Binary Tree
// 			https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
//code
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    
    public String preOrder(TreeNode root,String str){
        if(root == null){
            str = str + "null,";
        }else{
            
            str = str + str.valueOf(root.val) + ",";
            str = preOrder(root.left,str);
            str = preOrder(root.right,str);
            
        }
        return str;
    }
    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
     
        return preOrder(root,"");
        
    }
    
    public TreeNode des(List<String> data){
       
            if(data.get(0).equals("null")){
                data.remove(0);
                return null;
            }
               
                TreeNode root = new TreeNode(Integer.valueOf((data.get(0))));
                data.remove(0);
                //data.forEach(n -> System.out.println(n));
                root.left = des(data);
                root.right = des(data);
                return root;
  
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) { 
     //   TreeNode root = new TreeNode(0);
        
        String[] data1 = data.split(",");
        List<String> data2 = new ArrayList<>(Arrays.asList(data1));
        
        
        return des(data2);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
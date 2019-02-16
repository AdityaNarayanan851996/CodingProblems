                     // Q.) Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given node in a 
                     //     binary search tree where each node has a link to its parent.
                     //     https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1
 
/*Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.*/

/*Complete the function below
Node is as follows:
class Node{
	int data;
	Node left,right;
	Node(int d){
		data=d;
		left=right=null;
	}
}
*/
class GfG
{
    List<Integer> l = new ArrayList<>();
    List<Node> lr = new ArrayList<>();
    public void inOrder(Node root){
        if(root !=null){
            
            inOrder(root.left);
            l.add(root.data);
            lr.add(root);
            inOrder(root.right);
        }
    }
	public Node inorderSuccessor(Node root,Node k)
         {
             inOrder(root);
             //System.out.println(l);
             for(int i=0;i<l.size();i++){
                 if(l.get(i) == k.data){
                     if(i == l.size()-1){
                         return new Node(-1);
                     }else{
                         return lr.get(i+1);
                     }
                 }
             }
             return new Node(-1);
          //add code here.
         }
}

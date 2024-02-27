/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private int maximum;
    public Solution(){
        maximum = 0;
    }
    private int Solve(TreeNode node){
        if(node==null){
            return 0;
        }
        var l = Solve(node.left);
        var r = Solve(node.right);
        maximum = Math.Max(maximum,1+l+r);
        return 1+Math.Max(l,r);
    }
    public int DiameterOfBinaryTree(TreeNode root) {
        Solve(root);
        return maximum-1;
    }
}
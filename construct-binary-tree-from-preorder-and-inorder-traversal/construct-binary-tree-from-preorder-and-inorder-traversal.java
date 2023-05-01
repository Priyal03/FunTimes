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
    int preorderIndex;
    Map<Integer, Integer> inorderIndexMap;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        preorderIndex=0;
        inorderIndexMap = new HashMap<>();
        for(int i=0;i<inorder.length;i++){
            inorderIndexMap.put(inorder[i],i);
        }
        return construct(preorder, 0, preorder.length-1);
    }
    //this left and right pointers are here to search in Inorder list.
    public TreeNode construct(int[] preorder, int left, int right){
        if(left>right) 
            return null;
      
        int val = preorder[preorderIndex];
        TreeNode newNode = new TreeNode(val);
        preorderIndex++; //increase the index before starting recursion.

        newNode.left = construct(preorder, left, inorderIndexMap.get(val)-1);
        newNode.right = construct(preorder, inorderIndexMap.get(val)+1, right);
        
        return newNode;
    }
}
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
 * } //DFS solution 
 */
class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        List<List<Integer>> result = new ArrayList<>();
        if(root==null)
            return result;
        dfs(root,result,0);
        return result;
    }

    public void dfs(TreeNode root, List<List<Integer>> result, int level){
        
        if(root==null)
            return;
        
        if(level >= result.size()){
            result.add(new ArrayList<Integer>());//add a storage for new level
        }

        if(level%2==0){
            result.get(level).add(root.val);//leftToRight
        }else{
            result.get(level).add(0,root.val);//!leftToRight
        }

        dfs(root.left,result,level+1);
        dfs(root.right,result,level+1);
    }
}
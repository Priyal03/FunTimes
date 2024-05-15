# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    longest = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter(root)
        return self.longest

    def diameter(self, root:Optional[TreeNode]) -> int:

        if root is None:
            return 0

        else:
            left = self.diameter(root.left)
            right = self.diameter(root.right)
            self.longest = max(self.longest,left+right)

        return 1+max(left,right)
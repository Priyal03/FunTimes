# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        diff = abs(self.height(root.left)-self.height(root.right))
        if diff > 1:
            return False
        else:
            return True and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root:Optional[TreeNode]):
        if root is None:
            return -1
        elif root.left and root.right is None:
            return 1
        else:
            left = self.height(root.left)
            right = self.height(root.right)
            return max(left,right)+1

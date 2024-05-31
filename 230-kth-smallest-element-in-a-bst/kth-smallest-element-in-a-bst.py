# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, node: Optional[TreeNode], k: int) -> int:
        inorder = []

        def traversal(root):
            if root.left:
                traversal(root.left)
            inorder.append(root.val)
            if root.right:
                traversal(root.right)

        traversal(node)
        return inorder[k - 1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root:
            stack.append((1,root))
        depth=0
        while stack:
            level, root=stack.pop()
            if root:
                depth=max(depth,level)
                stack.append((level+1, root.left))
                stack.append((level+1, root.right))

        return depth
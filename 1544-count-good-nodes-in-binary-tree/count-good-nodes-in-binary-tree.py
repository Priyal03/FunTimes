# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0

    def dfs(self, node, m):
        if not node:
            return
        if node.val >= m:
            self.count += 1
            m = node.val

        self.dfs(node.left, m)
        self.dfs(node.right, m)

    def goodNodes(self, rooTreeNode) -> int:

        self.dfs(rooTreeNode, float("-inf"))
        return self.count

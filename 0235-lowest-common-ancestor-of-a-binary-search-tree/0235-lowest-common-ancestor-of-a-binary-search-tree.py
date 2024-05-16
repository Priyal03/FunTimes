# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parentvalue = root.val
        pvalue = p.val
        qvalue = q.val

        if pvalue<parentvalue and qvalue<parentvalue:
            return self.lowestCommonAncestor(root.left, p, q)
        elif pvalue>parentvalue and qvalue>parentvalue:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
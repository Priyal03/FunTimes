# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
# Parent Pointers:
# We use a dictionary parent to store the parent of each node. Initially, we store the root with None as its parent.
# We use a stack to traverse the tree iteratively (similar to depth-first search). For each node, we record its parent.
# Finding Ancestors:
# Once we have the parent pointers, we trace all ancestors of p (starting from p and moving upwards using the parent dictionary) and store them in a set ancestors.
# Finding LCA:
# Then, we move upwards from q using the parent dictionary. The first ancestor of q that is also in the ancestors set (which contains the ancestors of p) is the lowest common ancestor.

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent={root:None}
        stack=[root]

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left]=node
                stack.append(node.left)
            if node.right:
                parent[node.right]=node
                stack.append(node.right)

        ancestors = set()

        while p:
            ancestors.add(p)
            p=parent[p]

        while q not in ancestors:
            q=parent[q]
        
        return q
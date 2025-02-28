# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = deque([(root,1)]) #we are counting node length in this problem rather than a depth.

        while queue:

            currNode, depth = queue.popleft()

            if currNode.left is None and currNode.right is None:
                return depth # leaf node has no children.

            #traverse when one of the child is present.
            if currNode.left:
                queue.append((currNode.left,depth+1))

            if currNode.right:
                queue.append((currNode.right,depth+1))
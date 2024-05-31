# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        
        queue = collections.deque()
        queue.append(root)

        while queue:
            level=[]
            length = len(queue)

            for i in range(length):
                element = queue.popleft()
                if element:
                    level.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
            if level:        
                ans.append(level)
        return ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = collections.deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                element = queue.popleft()
                #adding left and right checks because we do not want false positives with Null nodes
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            # add the last element on that level, that is the right most element.
            
            res.append(element.val)
        return res

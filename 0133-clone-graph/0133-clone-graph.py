"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodemap={}

        def myCloneFunc(node):
            if not node:
                return
            if node in nodemap:
                return nodemap[node]
            
            current = Node(node.val)
            nodemap[node]=current
            for x in node.neighbors:
                current.neighbors.append(myCloneFunc(x))

            return current

        return myCloneFunc(node)
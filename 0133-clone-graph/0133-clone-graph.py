"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    nodemap = {}

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return
        if node in self.nodemap:
            return self.nodemap[node]

        clonedNode = Node(node.val)
        self.nodemap[node] = clonedNode
        for x in node.neighbors:
            clonedNode.neighbors.append(self.cloneGraph(x))

        return clonedNode

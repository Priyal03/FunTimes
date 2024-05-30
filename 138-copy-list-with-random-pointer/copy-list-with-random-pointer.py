"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    visited = {}
    def getClonedNode(self, node):
        if not node:
            return None
        if node not in self.visited:
            self.visited[node] = Node(node.val, None, None)
        return self.visited[node]
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head
        old_node = head
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node
        while old_node:
            new_node.next = self.getClonedNode(old_node.next)
            new_node.random = self.getClonedNode(old_node.random)
            old_node = old_node.next
            new_node = new_node.next
        return self.visited[head]
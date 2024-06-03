class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        length = len(edges)
        if length != (n - 1):  # need exactly n-1 edges to make noncyclic tree
            return False
        parent = [num for num in range(n)]

        def find(element):
            while element != parent[element]:
                element = parent[element]
            return element

        def union(first, second):
            firstparent = find(first)
            secondparent = find(second)
            if firstparent == secondparent:
                return False
            else:
                parent[secondparent] = firstparent
                return True

        for x, y in edges:
            if not union(x, y):
                return False
        return True

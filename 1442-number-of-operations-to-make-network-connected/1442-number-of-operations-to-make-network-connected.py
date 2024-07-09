class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges=len(connections)
        if edges<(n-1):
            return -1
        parent=list(range(n))
        self.connectedEdges=0

        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx!=rooty:
                parent[rootx]=rooty
                self.connectedEdges+=1

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        for x,y in connections:
            union(x,y)

        return n-1-self.connectedEdges
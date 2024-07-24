class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(list)
        cset = set()
        for a, b in connections:
            adjList[a].append(b)
            adjList[b].append(a)
            cset.add((a, b))

        invertedEdges = 0
        queue = deque([0])
        visited = set()
        while queue:
            node = queue.popleft()
            visited.add(node)
            for x in adjList[node]:
                if x not in visited:
                    if (node, x) in cset:
                        invertedEdges += 1
                    queue.append(x)

        return invertedEdges

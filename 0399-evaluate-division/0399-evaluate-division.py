class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adjList = defaultdict(list)  # map a to b,value[i]
        for i, val in enumerate(equations):
            a, b = val
            adjList[a].append([b, values[i]])
            adjList[b].append([a, 1 / values[i]])

        def bfs(source, dest):
            if source not in adjList or dest not in adjList:
                return -1
            q = deque()
            q.append([source, 1])
            visited = set()
            visited.add(source)
            while q:
                node, weight = q.popleft()
                if node == dest:
                    return weight
                for n, w in adjList[node]:
                    if n not in visited:
                        
                        visited.add(n)
                        q.append([n, w * weight])
            
            return -1

        ans = []
        for query in queries:
            ans.append(bfs(query[0], query[1]))
        return ans

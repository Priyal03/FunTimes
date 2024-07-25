class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        seen = [0] * len(graph)

        for i in range(len(graph)):
            if seen[i] == 0:
                queue = deque([i])
                seen[i] = -1
                while queue:
                    node = queue.popleft()
                    for x in graph[node]:
                        if seen[x] == 0:
                            seen[x] = -1 * seen[node]
                            queue.append(x)
                        elif seen[x] == seen[node]:
                            return False
        return True

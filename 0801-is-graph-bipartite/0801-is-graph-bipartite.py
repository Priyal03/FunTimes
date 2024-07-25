class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in color:
                    color[neighbor] = color[node] ^ 1
                    if not dfs(neighbor):
                        return False
                elif color[neighbor] == color[node]:
                    return False
            return True

        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                if not dfs(node):
                    return False

        return True

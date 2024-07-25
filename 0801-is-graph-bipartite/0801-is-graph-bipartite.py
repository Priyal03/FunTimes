class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        colored = {}
        vertices = len(graph)

        for i in range(vertices):
            if i not in visited:
                if self.dfs(i , graph , colored , 0 , visited) == 0:
                    return 0
        
        return 1
    
    def dfs(self , node , graph , colored , color , visited):
        visited.add(node)
        colored[node] = color
        
        for nei in graph[node]:
            if nei not in visited:
                if self.dfs(nei , graph , colored , not color , visited) == 0:
                    return 0
            elif colored[nei] == color:
                return 0
        
        return 1
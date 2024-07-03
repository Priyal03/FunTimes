class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cities = len(isConnected)
        visited = set()

        def dfs(city):
            visited.add(city)
            
            for c, connection in enumerate(isConnected[city]):
                if connection == 1 and c not in visited:
                    dfs(c)

        provinces = 0
        for c in range(cities):
            if c not in visited:
                dfs(c)
                provinces += 1

        return provinces

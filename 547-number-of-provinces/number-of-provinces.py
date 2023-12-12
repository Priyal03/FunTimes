class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provincesCount = 0
        def search(position):
            visited.add(position)
            for i in range(len(isConnected[position])):
                if i not in visited and isConnected[position][i] == 1:
                    search(i)

        for i in range(len(isConnected)):
            if i in visited:
                continue
            else:
                provincesCount +=1
                search(i)

        return provincesCount
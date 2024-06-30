class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        dependencyList = [0]*numCourses
        result = []
        for course, prereq in prerequisites:
            dependencyList[course]+=1
            adjList[prereq].append(course)
        queue=deque()
        for i in range(numCourses):
            if dependencyList[i]==0:
                queue.append(i)
        while queue:
            node = queue.pop()
            result.append(node)
            for x in adjList[node]:
                dependencyList[x]-=1
                if dependencyList[x]==0:
                    queue.append(x)
                    
        return result if len(result)==numCourses else []
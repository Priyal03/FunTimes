class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyList = [0]*numCourses
        adjList = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            dependencyList[course]+=1
            adjList[prereq].append(course)
        
        queue=deque()
        for i in range(numCourses):
            if dependencyList[i]==0:
                queue.append(i)

        total=0
        while queue:
            prereq=queue.pop()
            total+=1
            for c in adjList[prereq]:
                dependencyList[c]-=1
                if dependencyList[c]==0:
                    queue.append(c)

        return total==numCourses

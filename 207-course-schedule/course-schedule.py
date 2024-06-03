#from collections import dict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjmatrix = [[] for _ in range(numCourses)]
        indegree =[0]*numCourses
        for x,y in prerequisites:
            adjmatrix[y].append(x)
            indegree[x]+=1
        queue=deque()    
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i) 
        coursestaken=0
        while queue:
            node = queue.popleft()
            coursestaken+=1
            for neighbor in adjmatrix[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return coursestaken == numCourses
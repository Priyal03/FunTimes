class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        dependents=[0]*(n)
        prereqsTo=[[] for _ in range(n)]

        for course, prereq in prerequisites:
            dependents[course]+=1
            prereqsTo[prereq].append(course)

        queue=deque()
        ans=[]

        for i in range(n):
            if dependents[i]==0:
                queue.append(i)
                
        while queue:
            node = queue.popleft()
            ans.append(node)
            for curr in prereqsTo[node]:
                dependents[curr]-=1
                if dependents[curr]==0:
                    queue.append(curr)
                    
        return ans if len(ans)==n else []
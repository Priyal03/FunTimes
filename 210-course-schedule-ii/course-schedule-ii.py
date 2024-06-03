from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        matrix = [[] for _ in range(numCourses)]
        dependencyList = [0] * (numCourses)
        ans = []
        for course, prereq in prerequisites:
            matrix[prereq].append(course)
            dependencyList[course] += 1

        queue = deque(
            [course for course, count in enumerate(dependencyList) if count == 0]
        )
        while queue:
            course = queue.popleft()
            ans.append(course)
            for neighbors in matrix[course]:
                dependencyList[neighbors] -= 1
                if dependencyList[neighbors] == 0:
                    queue.append(neighbors)

        return (ans if len(ans) == numCourses else [])

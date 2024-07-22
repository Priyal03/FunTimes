class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        peopleWhoTrusts = defaultdict(list)
        indegree = [0] * (n + 1)

        for i in range(len(trust)):
            peopleWhoTrusts[trust[i][0]].append(trust[i][1])
            indegree[trust[i][1]] += 1

        for x in range(1, n + 1):
            if x not in peopleWhoTrusts and indegree[x] == (n - 1):
                return x

        return -1

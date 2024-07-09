class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parent[rootx] = rooty

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])
#look for invalid case
        for eq in equations:
            if eq[1] == "!" and (find(eq[0]) == find(eq[3])):
                return False
#if not, all are good cases.
        return True

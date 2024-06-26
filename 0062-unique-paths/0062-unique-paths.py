class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastrow = [1] * n

        for i in range(m - 1, 0, -1):  # as the last col values are 1 for all

            currentrow = [1] * n
            for j in range(n - 2, -1, -1):  # as the last row values are 1 for all . base condition.

                currentrow[j] = lastrow[j] + currentrow[j + 1]

            lastrow = currentrow

        return lastrow[0]
class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:

        def calculate(i):

            if manager[i] != -1:

                informTime[i] += calculate(manager[i])
                manager[i] = -1

            return informTime[i]

        return max(calculate(i) for i in range(n))

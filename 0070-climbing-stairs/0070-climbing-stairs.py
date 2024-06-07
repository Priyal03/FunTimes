class Solution:

    def climbStairs(self, n: int) -> int:
        memo=[0]*(n+1)
        return self.climb(0, n, memo)

    def climb(self, steps, n, memo) -> int:

        if steps == n:
            return 1
        elif steps > n:
            return 0

        if memo[steps]>0:
            return memo[steps]
        
        memo[steps]=self.climb(steps + 1, n, memo) + self.climb(steps + 2, n, memo)

        return memo[steps]

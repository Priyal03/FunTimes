class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        self.n = len(cost)
        memo=[0]*(self.n+1)
        
        return min(self.calculate(0,cost,memo),self.calculate(1,cost,memo))

    def calculate(self,i,cost,memo):
        
        if i>=self.n:
            return 0
        
        if memo[i]>0:
            return memo[i]

        memo[i] = cost[i]+min(self.calculate(i+1,cost,memo),self.calculate(i+2,cost,memo))

        return memo[i]

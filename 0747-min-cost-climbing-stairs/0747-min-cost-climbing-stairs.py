class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        
        stepOneCost=0
        stepTwoCost=0
        
        finalCost=0
        for i in range(2,n+1):
            
            finalCost = min(stepOneCost+cost[i-1],stepTwoCost+cost[i-2])

            stepTwoCost = stepOneCost
            stepOneCost = finalCost


        return finalCost
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp=[-1]*(n+1)
        dp[-1]=0
        dp[0]=nums[0]
        
        for i in range(1,n):
            
            if dp[i]>=0:
                continue

            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
    
        return dp[n-1]
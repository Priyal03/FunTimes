class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo=[-1]*(n+1)

        def calculate(i):
            if i>=n:
                return 0

            if memo[i]>=0:
                return memo[i]

            memo[i] = max(nums[i]+calculate(i+2),calculate(i+1))
            return memo[i]
        
        return calculate(0)

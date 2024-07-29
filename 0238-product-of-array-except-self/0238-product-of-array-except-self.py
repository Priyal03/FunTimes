class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        result=[1]*n

        for i in range(1,n):
            result[i]=nums[i-1]*result[i-1]

        multiplier=1
        for i in range(n-1,-1,-1):
            #multiplier variable will carry multiplication from right side. 
            result[i]*=multiplier
            #and it will keep multiplying as it progresses from right side to the left side
            multiplier*=nums[i]

        return result
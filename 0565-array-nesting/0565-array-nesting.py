class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans=0
        
        for i in range(len(nums)):
            count=0
            while i!=100001:
                
                temp=i
                count+=1
                
                i=nums[i]
                nums[temp]=100001 
                #float('inf')

            ans=max(ans,count-1)

        return ans

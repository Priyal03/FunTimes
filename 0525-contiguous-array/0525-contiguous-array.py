class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        startIndexMap={}
        startIndexMap[0]=-1
        ans=0
        count=0

        for i in range(len(nums)):
            
            count+= -1 if nums[i]==0 else 1

            if count in startIndexMap:
                ans = max(ans,i-startIndexMap[count])
            else:
                startIndexMap[count]=i

        return ans
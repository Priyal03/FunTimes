class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans=0
        visited = set()
        for i in range(len(nums)):
            count=0
            while i not in visited:
                visited.add(i)
                i=nums[i]
                count+=1

            ans=max(ans,count)

        return ans

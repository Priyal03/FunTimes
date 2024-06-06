class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        nums.sort()

        def backtrack(i):
            if len(nums)==i:
                ans.append(curr[:])
                return
            
            curr.append(nums[i])            
            backtrack(i+1)            
            curr.pop()
#simply skip the computations when there's duplicate
            while i < len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1)

        backtrack(0)
        return ans
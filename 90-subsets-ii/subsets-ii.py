class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        curr=[]
        nums.sort()
        def backtrack(i):
            if len(nums)==i:
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            if curr not in ans:
                backtrack(i+1)
            
            curr.pop()
            if curr not in ans:
                backtrack(i+1)

        backtrack(0)
        return ans
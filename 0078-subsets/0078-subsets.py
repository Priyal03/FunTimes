class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        subset=[]

        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy()) #breaking the recursion and storing results.
                return

            subset.append(nums[i])#taking in current element
            dfs(i+1)

            subset.pop() #not considering current element
            dfs(i+1)

        dfs(0)
        return ans
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def dfs(start, sublist, sum):
            if sum == target:
                ans.append(sublist.copy())
                return
            if sum > target or start >= len(candidates):
                return
            
            for i in range(start,len(candidates)):
                if candidates[i]>target:
                    break
                sublist.append(candidates[i])
                dfs(i, sublist, sum + candidates[i])
                sublist.pop()
            

        dfs(0, [], 0)
        return ans

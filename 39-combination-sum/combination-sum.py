class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def dfs(i, sublist, sum):
            if sum == target:
                ans.append(sublist.copy())
                return
            if sum > target or i >= len(candidates):
                return
            sublist.append(candidates[i])
            dfs(i, sublist, sum + candidates[i])
            sublist.pop()
            dfs(i + 1, sublist, sum)

        dfs(0, [], 0)
        return ans

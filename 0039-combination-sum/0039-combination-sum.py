class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()

        def compute(start,subset,sumTotal):
            if sumTotal==target:
                ans.append(subset.copy())
                return
            if sumTotal > target or start>= len(candidates):
                return

            for i in range(start, len(candidates)):
                if candidates[i]>target:
                    break
                subset.append(candidates[i])
                compute(i,subset,sumTotal+candidates[i])
                subset.pop()


        compute(0,[],0)
        return ans
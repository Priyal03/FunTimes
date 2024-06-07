class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans=[]
        candidates.sort()

        def backtrack(start,sum,sublist):
            if sum==target:
                ans.append(sublist[:])
                return
            if start==len(candidates) or sum>target:
                return

            for index in range(start, len(candidates)):
                #handling duplicate candidates
                if index>start and candidates[index]==candidates[index-1]:
                    continue
                #removing unnecessary computation
                if candidates[index]>target:
                    break
                #adding to sublist once and removing before moving on to next possibility
                sublist.append(candidates[index])
                backtrack(index+1,sum+candidates[index],sublist)
                sublist.pop()

        backtrack(0,0,[])
        return ans
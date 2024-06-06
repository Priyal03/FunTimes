class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n=len(nums)
        curr=[]
        
        def backtrack(i,curr):
            if i>n:
                return
            if len(curr)==n:
                result.append(curr[:])
                return
            
            for allx in nums:
                if allx not in curr:
                    curr.append(allx)
                    backtrack(i+1,curr)
                    curr.pop()

        backtrack(0,[])
        return result
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        
        def countones(x):
            total=0
            while x!=0:
                total+=1
                x&=(x-1)
            return total

        for i in range(n+1):
            ans.append(countones(i))

        return ans
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        powerof2=1

        while powerof2 <= n :
            
            i=0
            while i < powerof2 and i+powerof2 <= n :
                
                ans[i+powerof2]=ans[i]+1
                i+=1
            
            powerof2<<=1 

        return ans
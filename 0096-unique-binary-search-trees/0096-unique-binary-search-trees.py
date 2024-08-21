class Solution:
    def numTrees(self, n: int) -> int:
        
        uniqueBST=[0]*(n+1)
        uniqueBST[0]=1
        uniqueBST[1]=1

        for i in range(2,n+1):
            for j in range(1,i+1):
                uniqueBST[i]+=uniqueBST[j-1]*uniqueBST[i-j]

        return uniqueBST[n]
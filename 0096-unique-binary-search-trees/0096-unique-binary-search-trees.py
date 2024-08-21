class Solution:
    def numTrees(self, n: int) -> int:
        
        catalanNumber = 1
        # formula --- 2(2n)*prev/(n+2)

        for i in range(n):
            catalanNumber = (2 * (i * 2 + 1)) * catalanNumber / (i + 2)

        return int(catalanNumber)

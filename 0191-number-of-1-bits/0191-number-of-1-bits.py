class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        totalones = 0

        for i in range(32):
            if (n&mask) != 0 :
                totalones+=1
                
            mask <<= 1

        return totalones
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        totalones = 0

        while n !=0 :

            totalones+=1
#bitwise end operation with n-1 value always flip the rightmost first 1 bit to zero, we can take count of how many times it flips to zero until it is finally zero and exit the loop.
            n &= (n-1)

        return totalones
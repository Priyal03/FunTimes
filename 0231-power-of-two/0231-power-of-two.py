class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
            
        rightmost = n & (-n)
        return rightmost == n
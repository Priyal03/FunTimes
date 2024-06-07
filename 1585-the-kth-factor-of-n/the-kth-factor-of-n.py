class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors=[1]
        for i in range(n+1,0,-1):
            if n%i==0:
                divide = (n//i)
                if divide not in factors:
                    factors.append(divide)
        
        if len(factors)<k:
            return -1
            
        return factors[k-1]

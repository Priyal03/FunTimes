class Solution:
    def validPalindrome(self, s: str) -> bool:                
        
        def check(lo, hi, removed=False):
            
            while lo < hi:
                
                if s[lo] != s[hi]:
                    if removed:
                        return False
                    return check(lo+1, hi, True) or check(lo, hi-1, True)
                
                lo += 1
                hi -= 1
            
            return True

        return check(0, len(s)-1, False)
        
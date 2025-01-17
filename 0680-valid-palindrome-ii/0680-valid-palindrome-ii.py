class Solution:
    def checkPalindrome(self,s,i,j)->bool:
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        n=len(s)-1
        i=0
        
        while i<n:
            if s[i]!=s[n]:
                return self.checkPalindrome(s,i,n-1) or self.checkPalindrome(s,i+1,n)
            i+=1
            n-=1
            
        return True
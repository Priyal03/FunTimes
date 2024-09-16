class Solution:
    ans = ""
    ansLength = 0

    def check(self, s:str, l:int, r:int):
        while l>=0 and r<len(s) and s[l]==s[r]:
            currLen = r-l+1
            if currLen > self.ansLength:
                self.ansLength = currLen
                self.ans = s[l:r+1]
            l-=1
            r+=1

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            self.check(s,i,i)
            self.check(s,i,i+1)
            
        return self.ans
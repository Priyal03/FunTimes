class Solution:
    longest=""
    def isPalindrome(self, s, start, end) -> str:
        while start>=0 and end<len(s) and s[start]==s[end]:
            start-=1
            end+=1
        return s[start+1:end]

    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            curr = self.isPalindrome(s,i,i)
            if len(curr)>len(self.longest):
                self.longest=curr
            curr = self.isPalindrome(s,i,i+1)
            if len(curr)>len(self.longest):
                self.longest=curr
        return self.longest
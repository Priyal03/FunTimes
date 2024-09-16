class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        ans=[0,0]

        for i in range(n):
            dp[i][i]=True

        for i in range(1,n):
            if s[i]==s[i-1]:
                dp[i-1][i]=True
                ans=[i-1,i]

        for length in range(2,n):
            for start in range(n-length):
                end = start+length
                #start to end are palindrome if start+1, end-1 are already palindrome.
                if s[start]==s[end] and dp[start+1][end-1]:
                    dp[start][end]=True
                    ans=[start,end]
        
        i,j=ans
        return s[i:j+1]
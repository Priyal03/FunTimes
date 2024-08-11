class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slen=len(s)
        tlen=len(t)

        if slen==0:
            return True
        if tlen<slen:
            return False

        dp=[[0]*(tlen+1)for _ in range(slen+1)]

        for col in range(1,tlen+1):
            for row in range(1,slen+1):
                if s[row-1]==t[col-1]:
                    dp[row][col]=dp[row-1][col-1]+1
                else:
                    dp[row][col]=max(dp[row][col-1], dp[row-1][col])
            if dp[slen][col]==slen:
                return True

        return False
        
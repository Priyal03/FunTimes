class Solution:
    res = ""
    resLength = 0

    def longestPalindrome(self, s: str) -> str:

        for i in range(len(s)):
            self.calculate(s, i, i)
            self.calculate(s, i, i + 1)
        return self.res

    def calculate(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            currLength = r - l + 1
            if currLength > self.resLength:
                self.res = s[l : r + 1]
                self.resLength = currLength
            l -= 1
            r += 1

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars=[None]*128
        l=r=0
        ans=0
        while r<len(s):
            right=s[r]
            index=chars[ord(right)]
            if index is not None and l<=index<r:
                l=index+1
            ans=max(ans,r-l+1)
            chars[ord(right)]=r #key,value pair of ASCII value of 'a' and then last occured index pos of that in string.
            r+=1
        return ans

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word=0
        i=len(s)-1
        while i>=0:
            if s[i]==' ' and word>0:
                break
            if s[i]!=' ':
                word+=1
            i-=1
        return word
                
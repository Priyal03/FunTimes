class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        ans=""
        for i in range(len(words)-1,-1,-1):
            if words[i]:
                ans+=(words[i])+(" ")
        return ans.strip()
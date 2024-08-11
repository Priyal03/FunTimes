class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # if s.isspace():
        #     return 0
        word = s.split()[-1]
        return len(word)
                
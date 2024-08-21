class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        occur = {}

        for i in range(len(s)):

            if s[i] in occur:
                left = max(occur[s[i]] + 1, left)

            maxlen = max(maxlen, i - left + 1)

            occur[s[i]] = i

        return maxlen

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxlen = 0
        occur = [None]*128

        for right in range(len(s)):

            if occur[ord(s[right])] is not None: #if you find again.
            
                left = max(occur[ord(s[right])] + 1, left)#update the left bound value.

            maxlen = max(maxlen, right - left + 1)

            occur[ord(s[right])] = right #save everytime.

        return maxlen

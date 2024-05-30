from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Create frequency maps for s1 and the initial window of s2
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        for i in range(len(s1)):
            s1_freq[s1[i]] += 1
            s2_freq[s2[i]] += 1

        # Check if the initial window matches
        if s1_freq == s2_freq:
            return True

        # Slide the window through s2
        for i in range(len(s1), len(s2)):
            # Remove the leftmost character from the window
            s2_freq[s2[i - len(s1)]] -= 1
            if s2_freq[s2[i - len(s1)]] == 0:
                del s2_freq[s2[i - len(s1)]]

            # Add the rightmost character to the window
            s2_freq[s2[i]] += 1

            # Check if the current window matches s1
            if s1_freq == s2_freq:
                return True

        return False

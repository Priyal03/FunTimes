class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longestString = 0
        start = 0
        freq = {}
        mostFrequentLength = 0

        for end in range(len(s)):

            letter = s[end]
            freq[letter] = freq.get(letter, 0) + 1
            mostFrequentLength = max(mostFrequentLength, freq[letter])

            slidingWindow = end - start + 1
            if slidingWindow > (k + mostFrequentLength):
                freq[s[start]] -= 1
                start += 1

            longestString = end - start + 1

        return longestString

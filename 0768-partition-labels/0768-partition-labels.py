class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastcharmap = {}
        ans = []

        for idx, c in enumerate(s):
            lastcharmap[c] = idx

        left = rightEnd=0
        for index, char in enumerate(s):

            rightEnd = max(rightEnd, lastcharmap[char])

            if index == rightEnd:
                ans.append(rightEnd - left + 1)
                left = index + 1

        return ans

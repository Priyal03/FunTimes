class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = []
        for curr in intervals:
            if not merged:
                merged.append(curr)
            elif curr[0] > merged[-1][1]:
                merged.append(curr)
            else:
                merged[-1][1] = max(merged[-1][1], curr[1])
        return merged

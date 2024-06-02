class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        merged = []
        for curr in intervals:
            if not merged or curr[0]>merged[-1][1]:
                merged.append(curr)
            else:
                merged[-1][1] = max(merged[-1][1], curr[1])
        return merged
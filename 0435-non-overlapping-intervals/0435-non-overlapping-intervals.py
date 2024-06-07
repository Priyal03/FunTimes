class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        count=0
        rightIndex=0
        for i in range(1,n):
            if intervals[i][0]<intervals[rightIndex][1]:
                count+=1
                if (intervals[i][1] < intervals[rightIndex][1]):
                    rightIndex=i
            else:
                rightIndex=i    

        return count
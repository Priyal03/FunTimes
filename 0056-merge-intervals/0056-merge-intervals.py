class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans=[[intervals[0][0],intervals[0][1]]]

        for i in range(len(intervals)):
            
            if ans[-1][1]>=intervals[i][0]:
                ans[-1][1]=max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])

        return ans
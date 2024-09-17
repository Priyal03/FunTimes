class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        minheap=[]
        heapq.heappush(minheap, intervals[0][1])

        for i in range(1,len(intervals)):
            minimum = minheap[0]
            #remove whenever starttime is greater than minimum top element as meeting room can be available after that time.
            if intervals[i][0]>=minimum:
                heapq.heappop(minheap)
            #keep pushing it in heap for every new intervals.    
            heapq.heappush(minheap, intervals[i][1])

        return len(minheap)
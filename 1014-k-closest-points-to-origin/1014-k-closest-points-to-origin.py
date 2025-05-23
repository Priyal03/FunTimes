class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        minHeap = []

        for x,y in points:
            dist = x*x + y*y
            minHeap.append((dist,x,y))

        heapq.heapify(minHeap)
        while k>0:
            dist,x,y=heapq.heappop(minHeap)
            result.append([x,y])
            k-=1
        return result
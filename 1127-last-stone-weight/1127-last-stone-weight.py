class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = []

        for x in stones:
            heapq.heappush(self.heap, -x)

        heapq.heapify(self.heap)

        while len(self.heap)>1:
            x=heapq.heappop(self.heap)
            y=heapq.heappop(self.heap)

            if x!=y:
                heapq.heappush(self.heap, x-y)

        return -heapq.heappop(self.heap) if self.heap else 0
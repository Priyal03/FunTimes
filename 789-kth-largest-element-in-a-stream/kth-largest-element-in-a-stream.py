class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.heap = []
        for val in nums:
            self.add(val)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k :
            heapq.heappop(self.heap)
        return self.heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.order=deque()

    def get(self, key: int) -> int:
        
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.order.remove(key)
        self.cache[key]=value
        self.order.append(key)
        # print(self.cache)

        if len(self.cache) > self.capacity:
            leastUsed = self.order.popleft()
            del self.cache[leastUsed]

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
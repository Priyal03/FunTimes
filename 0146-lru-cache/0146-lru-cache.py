class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.hashmap={}
        self.queue=deque()

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.queue.remove(key)
        self.queue.append(key)
        return self.hashmap[key]

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.queue.remove(key)

        self.hashmap[key]=value
        self.queue.append(key)
        
        if len(self.hashmap)>self.capacity:
            leastUsedKey = self.queue.popleft()
            del self.hashmap[leastUsedKey]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
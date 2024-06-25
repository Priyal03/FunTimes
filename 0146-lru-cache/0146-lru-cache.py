class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.left = LinkedNode(0,0)
        self.right = LinkedNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])#remove the key first from linkedlist
            self.insert(self.hashmap[key])#update the linkedlist by adding neew node at the right most end which is most recently used end
            return self.hashmap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])

        self.hashmap[key]=LinkedNode(key,value)
        self.insert(self.hashmap[key])
#prune your cache if it is exceeding capacity by removing left most node.
        if len(self.hashmap) > self.capacity:
            lruNode = self.left.next
            self.remove(lruNode)#remove from ll
            del self.hashmap[lruNode.key]#remove also from hashmap

    def remove(self, node):
        
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LinkedNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
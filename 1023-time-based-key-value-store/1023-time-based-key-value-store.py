from sortedcontainers import SortedDict


class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timemap:
            self.timemap[key] = SortedDict()

        self.timemap[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timemap:
            return ""

        pointer = self.timemap[key].bisect_right(timestamp)
        if pointer == 0:
            return ""

        return self.timemap[key].peekitem(pointer-1)[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

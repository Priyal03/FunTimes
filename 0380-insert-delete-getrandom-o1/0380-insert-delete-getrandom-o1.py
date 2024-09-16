class RandomizedSet:

    def __init__(self):
        self.map={}
        self.arr=[]

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val]=len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        index = self.map[val]
        lastValue = self.arr[-1]

        self.map[lastValue]=index
        self.arr[index]=lastValue

        del self.map[val]
        self.arr.pop() #just purge it at the end.
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
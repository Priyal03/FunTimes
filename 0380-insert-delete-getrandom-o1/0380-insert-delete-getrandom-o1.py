class RandomizedSet:
#take map to insert and delete in O(1) time but take array to get random in O(1) time as we can't use random lib for hashmap.
    def __init__(self):
        self.random_map={}
        self.array=[]

    def insert(self, val: int) -> bool:
        if val in self.random_map:
            return False

        self.array.append(val)
        self.random_map[val]=len(self.array)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.random_map:
            return False
        
        index=self.random_map[val]
        lastelement=self.array[-1]

        self.array[index]=lastelement
        self.random_map[lastelement]=index

        del self.random_map[val]
        self.array.pop()
        return True        

    def getRandom(self) -> int:
        return random.choice(self.array)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
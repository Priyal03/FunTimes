class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minValue = 0
        if not self.stack:
            minValue = val
        else:
            minValue = min(self.stack[-1][1], val)
        self.stack.append((val, minValue))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

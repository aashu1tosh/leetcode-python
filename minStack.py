class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(self.minStack[::-1], val))
        else:
            self.minStack.append(val)
            

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
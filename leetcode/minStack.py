class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

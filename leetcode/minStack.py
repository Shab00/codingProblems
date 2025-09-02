class MinStack:

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass

if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    print(obj.top())
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())

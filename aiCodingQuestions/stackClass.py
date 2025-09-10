class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        a = self.items.pop()
        return a

    def peek(self):
        a = self.items[-1]
        return a

    def is_empty(self):
        if self.items == []:
            return True
        return False

s = Stack()
s.push(1)
s.push(2)
print(s.pop())
print(s.peek())
print(s.is_empty())

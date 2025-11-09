class _Node:
    """Doubly-linked list node used internally by LRUCache."""
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = _Node()
        self.tail = _Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: _Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: _Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _move_to_head(self, node: _Node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> _Node:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            self._move_to_head(node)
        else:
            new_node = _Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]

if __name__ == "__main__":
    def run_commands(commands, args):
        obj = None
        outputs = []
        for cmd, a in zip(commands, args):
            if cmd == "LRUCache":
                obj = LRUCache(*a)
                outputs.append(None)
            elif cmd == "put":
                obj.put(*a)
                outputs.append(None)
            elif cmd == "get":
                outputs.append(obj.get(*a))
            else:
                raise ValueError(f"Unknown command {cmd}")
        return outputs

    cmds1 = ["LRUCache", "put", "get",  "put", "put", "get", "get"]
    args1 = [[2], [1, 10], [1], [2, 20], [3, 30], [2], [1]]
    out1 = run_commands(cmds1, args1)
    print("Example 1 outputs:", out1)
    print("Example 1 expected:", [None, None, 10, None, None, 20, -1])
    print()

    cmds2 = ["LRUCache", "put", "put", "get", "put", "get", "get"]
    args2 = [[1], [1, 1], [1, 2], [1], [2, 3], [1], [2]]
    out2 = run_commands(cmds2, args2)
    print("Extra test 1 outputs:", out2)
    print("Extra test 1 expected:", [None, None, None, 2, None, -1, 3])
    print()

    cmds3 = ["LRUCache","put","put","get","put","get","get"]
    args3 = [[2],[1,1],[2,2],[1],[3,3],[2],[3]]
    out3 = run_commands(cmds3, args3)
    print("Extra test 2 outputs:", out3)
    print("Extra test 2 expected:", [None, None, None, 1, None, -1, 3])
    print()

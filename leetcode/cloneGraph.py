import copy

class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone(node: Node) -> Node:
    if not node:
        return None
    hashm = {}
    hashm[node] = Node(node.val)
    stack = [node]
    while stack:
        org = stack.pop()
        for n in org.neighbors:
            if n not in hashm:
                hashm[n] = Node(n.val)
                stack.append(n)
            hashm[org].neighbors.append(hashm[n])
    return hashm[node]


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

clone(node1)

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]    
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return True

obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))

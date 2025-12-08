class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDict(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word):
        def dfs(node, i):
            if node is None:
                return False
            if i == len(word):
                return node.is_end
            ch = word[i]
            if ch == '.':
                # try all children
                for child in node.children:
                    if child is not None and dfs(child, i + 1):
                        return True
                return False
            else:
                idx = ord(ch) - ord('a')
                child = node.children[idx]
                return dfs(child, i + 1)
        return dfs(self.root, 0)

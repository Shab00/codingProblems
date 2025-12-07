class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class WordDict(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        pass

    def search(self, word):
        pass

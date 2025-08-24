class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()
            current = current.children[ch]
        current.isEnd = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True
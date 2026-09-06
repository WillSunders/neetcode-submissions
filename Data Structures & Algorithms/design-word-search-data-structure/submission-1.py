class Trie:
    __slots__ = ("children", "end")
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = Trie()
            cur = cur.children[l]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(node: Trie, word:str, start:int) -> bool:
            cur = node
            for i in range(start, len(word)):
                l = word[i]
                if l == '.':
                    for c in cur.children.values():
                        if dfs(c, word, i + 1):
                            return True
                    return False
                if l not in cur.children:
                    return False
                cur = cur.children[l]
            return cur.end
        return dfs(self.root, word, 0)
        

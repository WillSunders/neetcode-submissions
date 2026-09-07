class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie():
            def __init__(self):
                self.children = {}
                self.end = False
        class PrefixTrie():
            def __init__(self):
                self.root = Trie()
            def insert(self, word:str):
                curr = self.root
                for l in word:
                    if l not in curr.children:
                        curr.children[l] = Trie()
                    curr = curr.children[l]
                curr.end = True
                
        vals = PrefixTrie()
        for word in words:
            vals.insert(word)
        cols = len(board[0])
        rows = len(board)
        res, path = [],[]
        visited = [[False] * cols for _ in range(rows)]
        def search(r:int, c:int, node:Trie):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if visited[r][c]:
                return
            if board[r][c] in node.children:
                node = node.children[board[r][c]]
                path.append(board[r][c])
                visited[r][c] = True
                if node.end:
                    res.append("".join(path))
                    node.end = False
                search(r+1, c, node)
                search(r-1, c, node)
                search(r, c+1, node)
                search(r, c-1, node)
                visited[r][c] = False
                path.pop()
        for c in range(cols):
            for r in range(rows):
                search(r, c, vals.root)
        return res
                
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj = defaultdict(list)
        bridges = defaultdict(list)
        wordList.append(beginWord)
        visited = set(beginWord)
        for word in wordList:
            for i in range(len(word)):
                chars = list(word)
                chars[i] = '*'
                nword = "".join(chars)
                adj[nword].append(word)
                bridges[word].append(nword)
        
        q = deque([(beginWord, 1)])
        while q:
            word, c = q.popleft()
            for bridge in bridges[word]:
                for nw in adj[bridge]:
                    if nw == endWord:
                        return c + 1
                    if nw != word and nw not in visited:
                        q.append((nw, c + 1))
                        visited.add(nw)
        return 0




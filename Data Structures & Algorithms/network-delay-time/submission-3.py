class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        connect = defaultdict(list)
        for s, trg, t in times:
            connect[s].append((t, trg))
        h = [(0, k)]
        while h:
            time, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            for t, nb in connect[node]:
                if nb not in visited:
                    heapq.heappush(h, (time + t, nb))
        return - 1


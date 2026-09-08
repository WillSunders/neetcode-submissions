class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flow = []
        pacific = {}
        atlantic = {}
        rows, cols = len(heights), len(heights[0])
        q = deque()
        q2 = deque()

        for r in range(rows):
            q.append((r, 0))
            pacific[(r, 0)] = 1
            q2.append((r, cols -1))
            atlantic[(r, cols - 1)] = 1

        for c in range(1, cols):
            q.append((0, c))
            pacific[(0, c)] = 1
            q2.append((rows - 1, c - 1))
            atlantic[(rows - 1, c - 1)] = 1

        while q:
            r, c = q.popleft()
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + x, c + y
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in pacific and heights[nr][nc] >= heights[r][c]:
                    q.append((nr, nc))
                    pacific[(nr, nc)] = 1

        while q2:
            r, c = q2.popleft()
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + x, c + y
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in atlantic and heights[nr][nc] >= heights[r][c]:
                    q2.append((nr, nc))
                    atlantic[(nr, nc)] = 1

        for cell in atlantic:
            if cell in pacific:
                r, c = cell
                flow.append([r, c])
        return flow



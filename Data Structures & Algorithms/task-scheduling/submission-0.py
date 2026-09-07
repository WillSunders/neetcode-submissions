from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        nums = [-c for c in counts.values()]
        heapq.heapify(nums)
        time = 0
        q = deque()
        while(nums or q):
            time += 1
            if nums:
                curr = heapq.heappop(nums)
                curr += 1
                if curr < 0:
                    q.append([curr, time + n])
            if q and q[0][1] == time:
                heapq.heappush(nums,q.popleft()[0])
        return time
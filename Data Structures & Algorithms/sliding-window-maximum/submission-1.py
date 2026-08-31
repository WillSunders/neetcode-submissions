import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        head = 0
        tail = k - 1
        out = []
        heap = []
        for i in range(0, k - 1):
            heapq.heappush(heap, [-nums[i], i])
        while tail < len(nums):
            heapq.heappush(heap, [-nums[tail], tail])
            while heap[0][1] < head:
                heapq.heappop(heap)
            out.append(-heap[0][0])
            head += 1
            tail += 1
        return out

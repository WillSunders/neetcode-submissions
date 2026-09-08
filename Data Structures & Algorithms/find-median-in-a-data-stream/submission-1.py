class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if not self.big and not self.small:
            heapq.heappush(self.big, num)
        elif num > self.big[0]:
            heapq.heappush(self.big, num)
            if len(self.big) == len(self.small) + 2:
                val = -heapq.heappop(self.big)
                heapq.heappush(self.small, val)
        else:
            heapq.heappush(self.small, -num)
            if len(self.small) == len(self.big) + 2:
                val = -heapq.heappop(self.small)
                heapq.heappush(self.big, val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.big) + 1:
            return -self.small[0]
        elif len(self.small) + 1 == len(self.big):
            return self.big[0]
        else:
            return (-self.small[0] + self.big[0]) / 2
        
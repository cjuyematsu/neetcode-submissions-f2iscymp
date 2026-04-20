import heapq

class MedianFinder:

    def __init__(self):
        self.s = []
        self.b = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s, -num)

        heapq.heappush(self.b, -heapq.heappop(self.s))

        if len(self.b) > len(self.s):
            heapq.heappush(self.s, -heapq.heappop(self.b))

    def findMedian(self) -> float:
        if len(self.s) > len(self.b):
            return -self.s[0]
        else:
            return (self.b[0] - self.s[0]) / 2

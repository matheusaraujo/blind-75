#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def smallHeapMax(self) -> int:
        return -self.small[0]

    def largeHeapMin(self) -> int:
        return self.large[0]

    def smallHeapIsBigger(self) -> bool:
        return len(self.small) > len(self.large)

    def smallHeapIsUnbalanced(self) -> bool:
        return len(self.small) > len(self.large) + 1

    def largeHeapIsUnbalanced(self) -> bool:
        return len(self.large) > len(self.small)  +1

    def largeHeapIsBigger(self) -> bool:
        return len(self.large) > len(self.small)

    def fitsInLargeHeap(self, num) -> bool:
        return self.large and num > self.largeHeapMin()

    def pushToLargeHeap(self, num):
        heapq.heappush(self.large, num)

    def pushToSmallHeap(self, num):
        heapq.heappush(self.small, -num)

    def moveFromSmallHeapToLargeHeap(self):
        val = -heapq.heappop(self.small)
        heapq.heappush(self.large, val)

    def moveMoveLargeHeapToSmallHeap(self):
        val = heapq.heappop(self.large)
        heapq.heappush(self.small, -val)

    def addNum(self, num: int) -> None:
        if self.fitsInLargeHeap(num): self.pushToLargeHeap(num)
        else: self.pushToSmallHeap(num)

        if self.smallHeapIsUnbalanced():
            self.moveFromSmallHeapToLargeHeap()

        if self.largeHeapIsUnbalanced():
            self.moveMoveLargeHeapToSmallHeap()

    def findMedian(self) -> float:
        if self.smallHeapIsBigger(): return self.smallHeapMax()
        if self.largeHeapIsBigger(): return self.largeHeapMin()
        return (self.smallHeapMax() + self.largeHeapMin()) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end


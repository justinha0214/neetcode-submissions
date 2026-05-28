class MedianFinder:

    def __init__(self):
        # left and right heap split the numbers into half partitions
        self.left, self.right = [], []

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -1 * num)
        if len(self.left) > len(self.right) + 1: # partitions are unequal by more than one
            heapq.heappush(self.right, -1 * heapq.heappop(self.left))
        elif len(self.right) > len(self.left) + 1:
            heapq.heappush(self.left, -1 * heapq.heappop(self.right))
        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0] * -1
        elif len(self.right) > len(self.left):
            return self.right[0]
        else:
            return ((self.left[0] * -1) + (self.right[0])) / 2
        
        
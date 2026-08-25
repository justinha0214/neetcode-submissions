class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def findDist(x, y):
            return math.sqrt((x*x) + (y*y))
        
        heap = []
        for i in range(len(points)):
            d = findDist(points[i][0], points[i][1])
            heapq.heappush(heap, [-d, i])
            if len(heap) > k:
                heapq.heappop(heap)
        ans = [points[i] for d, i in heap]
        return ans
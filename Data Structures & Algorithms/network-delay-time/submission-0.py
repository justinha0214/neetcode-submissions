class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = defaultdict(list)
        for u, v, t in times:
            nodes[u].append((v, t))
        
        minHeap = [(0, k)]
        time = 0
        visited = set()
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = w1
            for n2, w2 in nodes[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        
        return time if len(visited) == n else -1
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxP = max(piles)
        l, r, k = 1, maxP, maxP
        while l <= r:
            mid = l + ((r-l) // 2)
            time = 0
            for p in piles:
                time += math.ceil(p / mid)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
                k = mid
        return k

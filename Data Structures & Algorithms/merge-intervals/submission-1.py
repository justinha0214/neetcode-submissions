class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            e1 = res[-1][1]
            s2, e2 = intervals[i]
            if s2 <= e1:
                res[-1][1] = max(e1, e2)
            else:
                res.append([s2, e2])
        return res

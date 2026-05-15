class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        sub = set()
        i = j = 0
        while i < len(s):
            while j < len(s) and s[j] not in sub:
                sub.add(s[j])
                j += 1
            res = max(res, len(sub))
            sub = set()
            i, j = i+1, i
        res = max(res, len(sub))
        return res
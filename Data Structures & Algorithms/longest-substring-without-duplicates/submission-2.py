class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l, res = 0, 0
        for r in range(len(s)):
            if s[r] not in window:
                res = max(res, r - l + 1)
            else: # we know s[r] is a dupe
                while l <= r and s[r] in window:
                    window.remove(s[l])
                    l += 1
            window.add(s[r])   
        return res
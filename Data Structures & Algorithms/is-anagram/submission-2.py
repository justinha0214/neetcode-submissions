class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a, b = "".join(sorted(s)), "".join(sorted(t))
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if a[i] != b[i]:
                return False
        return True
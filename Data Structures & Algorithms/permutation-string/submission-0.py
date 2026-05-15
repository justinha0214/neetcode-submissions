class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s3 = "".join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            s4 = "".join(sorted(s2[i:i+len(s1)]))
            if s3 == s4:
                return True
        return False
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        words = sorted(strs)
        for i in range(min(len(words[0]), len(words[-1]))):
            if words[0][i] != words[-1][i]:
                return words[0][:i]
        return words[0]
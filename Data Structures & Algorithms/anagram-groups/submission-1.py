class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            tmp = [0] * 26 # all lowercase letters
            for c in s:
                tmp[ord(c) - ord('a')] += 1
            anagrams[tuple(tmp)].append(s)
        return list(anagrams.values())
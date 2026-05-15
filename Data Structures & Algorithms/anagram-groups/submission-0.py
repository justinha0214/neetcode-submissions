class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # Create a dict of anagrams

        for s in strs: # iterate through every string
            count = [0] * 26 # a-z characters

            for c in s: # iterate through every character of the string
                count[ord(c) - ord("a")] += 1 # assign count to each alphabetical letter

            res[tuple(count)].append(s) # add to list of identical anagram by count of letters

        return list(res.values()) # return the groups of anagrams
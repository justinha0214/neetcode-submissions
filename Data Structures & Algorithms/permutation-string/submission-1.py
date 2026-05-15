class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): # edge case where s1 wouldn't fit in s2
            return False

        # Create hashMaps for each string to count the num of occurences within the sliding window
        count1, count2 = {}, {}
        for i in range(len(s1)): # calculate the starting sliding window
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

        # Sliding Window going through each substring of length s1 within s2
        for i in range(len(s1), len(s2)):
            if count1 == count2:
                return True
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

            left = s2[i - len(s1)]
            count2[left] -= 1
            if count2[left] == 0:
                count2.pop(left, None)
        # If permutation is last position of s2, need to check
        return count1 == count2
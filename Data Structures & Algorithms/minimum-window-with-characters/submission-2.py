class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s): # edge cases
            return ""
        
        # initialize t and window's counter hashMaps
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        # create have and need trackers, have will start at 0
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity") # dummy values to hold answer
        l = 0
        for r in range(len(s)): # loop in O(n) time by iterating to the right
            c = s[r]
            window[c] = 1 + window.get(c, 0) # add new right character to window

            if c in countT and window[c] == countT[c]: # check if new character is in t, if the count is met, increase have
                have += 1
            
            # shorten the window from the left while have == need
            while have == need:
                windowLen = r - l + 1
                if windowLen < resLen: # set new result range if it's shorter
                    res = [l, r]
                    resLen = windowLen
                window[s[l]] -= 1 
                if s[l] in countT and window[s[l]] < countT[s[l]]: # check to see if the character removed from the left was one of the t characters
                    have -= 1 
                l += 1 # slide forward left
        l, r = res 
        return s[l:r+1] if resLen != float("infinity") else ""
            
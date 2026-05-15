class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # use index, not value
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) # want to append the index rather than value for next step logic

            if l > q[0]: # if left pointer has surpassed the position of the max within the window
                q.popleft() # pop the max value
            
            if (r + 1) >= k: # once we've created the window, we want to append the max to output
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

            

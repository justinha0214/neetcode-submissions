class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0: # if nums[i] is positive, we know no negative numbers are ahead
                break
            if i > 0 and a == nums[i-1]: # skip dupes
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]]) 

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
                           


        # Two Pointer Approach:
        # [-1,0,1,2,-1,-4]
        # sorted: [-4, -1, -1, 0, 1, 2]
        #           i   j            k
        # -3 < 0
        # sorted: [-4, -1, -1, 0, 1, 2]
        #           i          j     k
        # -2 < 0
        # sorted: [-4, -1, -1, 0, 1, 2]
        #           i             j  k
        # -1 < 0
        # sorted: [-4, -1, -1, 0, 1, 2]
        #               i   j        k
        # 0 = 0, append to res
        # sorted: [-4, -1, -1, 0, 1, 2]
        #               i      j     k
        # 1 > 0
        # sorted: [-4, -1, -1, 0, 1, 2]
        #               i      j  k   
        # 0 = 0, append to res

        # loop 1 conditions: i < len(nums) - 2 (minimum 3 values needed)
        # loop 2 conditions: j < k 







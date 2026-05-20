class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1 2 3 4 5 6 7 8
        # 1 2 3 4 5
        # 1 1 2 2 3 3 4 4 5 5 6 7 8 , n = 13

        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        half, total = (len(A) + len(B)) // 2, len(A) + len(B)
        while True:
            midA = l + ((r-l) // 2)
            midB = half - midA - 2

            aRight = A[midA + 1] if midA < (len(A) - 1) else float("inf")
            aLeft = A[midA] if midA >= 0 else float("-inf")
            bRight = B[midB + 1] if midB < (len(B) - 1) else float("inf")
            bLeft = B[midB] if midB >= 0 else float("-inf")

            if aRight >= bLeft and aLeft <= bRight: # valid left-right partition
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = midA - 1
            else: # bLeft > aRight
                l = midA + 1

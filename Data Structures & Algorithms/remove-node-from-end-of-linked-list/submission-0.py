# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Brute Force, run through list and count, rerun and remove
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        if sz - n == 0:
            head = head.next
        else:
            curr, index = head, 0
            while index < sz - n - 1:
                curr = curr.next
                index += 1
            curr.next = curr.next.next
        return head
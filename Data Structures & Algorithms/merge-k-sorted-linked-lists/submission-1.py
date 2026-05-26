# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            tail = head = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next

            head.next = list1 or list2

            return tail.next
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoLists(lists[i-1], lists[i])
        
        return lists[-1] if len(lists) > 0 else None
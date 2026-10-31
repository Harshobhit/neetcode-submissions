# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr , l2_curr = list1, list2
        dummy = ListNode()
        head = dummy

        while l1_curr and l2_curr:
            if l1_curr.val <= l2_curr.val:
                dummy.next = l1_curr
                l1_curr = l1_curr.next
            else:
                dummy.next = l2_curr
                l2_curr = l2_curr.next
            
            dummy = dummy.next
            
        #Remaining elements list 1
        if l1_curr:
            dummy.next = l1_curr
        
        #Remaining elements list 2
        elif l2_curr:
            dummy.next = l2_curr
    
        return head.next
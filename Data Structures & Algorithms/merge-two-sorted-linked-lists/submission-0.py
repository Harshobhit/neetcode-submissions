# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr , l2_curr = list1, list2
        temp = None
        head = None

        while l1_curr and l2_curr:
            if l1_curr.val <= l2_curr.val:
                new_node = l1_curr
                l1_curr = l1_curr.next
            else:
                new_node = l2_curr
                l2_curr = l2_curr.next
            
            if not head:
                head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = new_node
        
        #Remaining elements list 1
        while l1_curr:
            new_node = l1_curr
            if not head:
                head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = new_node
            l1_curr = l1_curr.next
        
        #Remaining elements list 1
        while l2_curr:
            new_node = l2_curr
            if not head:
                head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = new_node
            l2_curr = l2_curr.next
        
        return head

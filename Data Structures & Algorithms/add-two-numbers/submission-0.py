# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Iterate to find largest
        large_ll = l1
        small_ll = l2

        curr_l1 = l1
        curr_l2 = l2

        while curr_l1 or curr_l2:
            if curr_l1 is None and curr_l2:
                large_ll = l2
                small_ll = l1
                break
            elif curr_l2 is None and curr_l1:
                large_ll = l1
                small_ll = l2
                break
            
            curr_l1 = curr_l1.next if curr_l1 else curr_l1
            curr_l2 = curr_l2.next if curr_l2 else curr_l2
        
        head = large_ll
        prev = None
        carry = 0
        while small_ll:
            curr_node_sum = carry + small_ll.val + large_ll.val
            if curr_node_sum >= 10:
                large_ll.val = curr_node_sum % 10
                carry = 1
            else:
                large_ll.val = curr_node_sum
                carry = 0
            
            prev = large_ll
            small_ll = small_ll.next
            large_ll = large_ll.next
        
        while large_ll:
            curr_node_sum = carry + large_ll.val
            if curr_node_sum >= 10:
                large_ll.val = curr_node_sum % 10
                carry = 1
            else:
                large_ll.val = curr_node_sum
                carry = 0
            prev = large_ll
            large_ll = large_ll.next
        
        if carry:
            prev.next = ListNode(carry)
        
        return head
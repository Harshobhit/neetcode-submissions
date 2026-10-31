# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_ll = 0
        tmp_curr = head

        while tmp_curr:
            len_ll += 1
            tmp_curr = tmp_curr.next

        if not head or (len_ll - n < 0):
            return head
        
        if (len_ll - n) == 0:
            head = head.next
        else:
            counter = -1
            prev = ListNode()
            curr = head

            while counter != (len_ll - n - 1):
                prev = curr
                curr = curr.next
                counter += 1
            
            prev.next = curr.next

        return head

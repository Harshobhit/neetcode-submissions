# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Finding middle node
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        prev = None

        while second_half:
            temp_next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp_next
        
        first = head
        second = prev

        while second:
            temp_next_first = first.next
            temp_next_second = second.next
            first.next = second
            second.next = temp_next_first
            first = temp_next_first
            second = temp_next_second

            
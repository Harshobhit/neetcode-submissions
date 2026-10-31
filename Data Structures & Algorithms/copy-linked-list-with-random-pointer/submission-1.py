"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        
        curr_node = head

        while curr_node:
            new_node = Node(curr_node.val, curr_node.next)
            curr_node.next = new_node
            curr_node = new_node.next
        
        new_head = head.next

        l1 = head

        #l1.next is random only
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        
        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l2.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next
        
        return new_head
        
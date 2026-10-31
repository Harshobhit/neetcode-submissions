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
        
        new_head = None
        curr_node = head
        old_new_node_map = {}

        while curr_node:
            new_node = Node(curr_node.val)
            if not new_head:
                new_head = new_node
            old_new_node_map[curr_node] = new_node

            curr_node = curr_node.next
        
        new_ll = new_head
        old_ll = head

        while old_ll:
            new_ll.next = old_new_node_map[old_ll.next] if old_ll.next else None
            new_ll.random = old_new_node_map[old_ll.random] if old_ll.random else None
            new_ll = new_ll.next
            old_ll = old_ll.next
        
        return new_head

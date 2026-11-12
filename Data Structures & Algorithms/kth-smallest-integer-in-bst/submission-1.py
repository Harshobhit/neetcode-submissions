# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_counter = 0
        node_stack = []
        curr = root

        while curr or node_stack:
            while curr:
                node_stack.append(curr)
                curr = curr.left
            
            node = node_stack.pop()
            node_counter += 1
            if node_counter == k:
                return node.val
            
            curr = node.right

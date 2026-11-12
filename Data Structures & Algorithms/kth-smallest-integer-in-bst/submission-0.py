# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse_in_order(self, node:TreeNode, nodes):
        if not node:
            return
        
        self.traverse_in_order(node.left, nodes)
        nodes.append(node.val)
        self.traverse_in_order(node.right, nodes)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.traverse_in_order(root, nodes)
        return nodes[k-1]
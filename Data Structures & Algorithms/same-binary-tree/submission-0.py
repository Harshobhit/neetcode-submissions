# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder_traversal(node, result):
            if not node:
                return
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)
        
        p_nodes = []
        q_nodes = []
        inorder_traversal(p, p_nodes)
        inorder_traversal(q, q_nodes)

        return p_nodes == q_nodes

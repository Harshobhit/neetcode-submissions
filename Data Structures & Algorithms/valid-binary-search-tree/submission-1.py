# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def in_order_traversal(self, root, nodes) -> list:
        if not root:
            return
        self.in_order_traversal(root.left, nodes)
        nodes.append(root.val)
        self.in_order_traversal(root.right, nodes)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []
        self.in_order_traversal(root, nodes)

        max_till_now = nodes[0]

        if len(nodes) >1:
            for index in range(1, len(nodes)):
                if nodes[index] <= max_till_now:
                    return False
                max_till_now = max(nodes[index], max_till_now)
        
        return True
            

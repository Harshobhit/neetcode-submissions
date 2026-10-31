# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height = 0
        def get_height(root):
            if not root:
                return 0
            
            left_tree_height = get_height(root.left)
            right_tree_height = get_height(root.right)

            self.height = abs(left_tree_height - right_tree_height)

            return 1 + max(left_tree_height, right_tree_height)
        
        get_height(root)
        return True if self.height <= 1 else False

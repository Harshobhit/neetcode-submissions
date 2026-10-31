# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_parent_node(self, node, val_to_insert):
        if node.left is None and node.right is None:
            return node

        if val_to_insert > node.val:
            return self.find_parent_node(node.right, val_to_insert)
        else:
            return self.find_parent_node(node.left, val_to_insert)
        
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            parent_node = self.find_parent_node(root, val)

            if val > parent_node.val:
                parent_node.right = TreeNode(val)
            else:
                parent_node.left = TreeNode(val)
        else:
            root = TreeNode(val)
    
        return root
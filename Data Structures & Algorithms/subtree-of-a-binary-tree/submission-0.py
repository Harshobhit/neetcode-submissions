# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    sub_tree_found = False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return 
        
        if root.val == subRoot.val:
            is_same = self.isSameTree(root, subRoot)
            if is_same and not self.sub_tree_found:
                self.sub_tree_found = True

        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)

        return self.sub_tree_found 
        

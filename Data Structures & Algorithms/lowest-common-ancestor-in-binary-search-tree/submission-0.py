# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_ancestors(self, root, node):
        curr = root
        acs = [curr]

        while curr != node:
            if curr.val > node.val:
                curr = curr.left
            else:
                curr = curr.right

            acs.append(curr)

        return acs[::-1]

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_acs = self.find_ancestors(root, p)
        q_acs = set(self.find_ancestors(root, q))


        for node in p_acs:
            if node in q_acs:
                return node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_good_nodes(self, curr_node, max_node_val, good_nodes):
        if not curr_node:
            return
        
        if curr_node.val >= max_node_val:
            good_nodes.append(curr_node)
            
        max_node_val = max(max_node_val, curr_node.val)
        self.check_good_nodes(curr_node.left, max_node_val, good_nodes)
        self.check_good_nodes(curr_node.right, max_node_val, good_nodes)

    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = []

        self.check_good_nodes(root, root.val, good_nodes)

        return len(good_nodes)
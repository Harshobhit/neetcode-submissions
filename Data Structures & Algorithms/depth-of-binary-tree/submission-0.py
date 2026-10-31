# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()

        if root:
            queue.append(root)
        else:
            return 0
        
        level = 1

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                elif curr.right:
                    queue.append(curr.right)
            level += 1
        
        return level
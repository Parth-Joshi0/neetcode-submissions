# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, lower, upper):
            if not node:
                return True
            if lower >= node.val:
                return False
            if upper <= node.val:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root.left, -float("inf"), root.val) and dfs(root.right, root.val, float("inf"))
                

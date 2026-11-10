# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodNodesMax(node, maximum):
            if not node:
                return 0
            res = 1 if node.val >= maximum else 0
            maximum = max(node.val, maximum)
            return res + goodNodesMax(node.left, maximum) + goodNodesMax(node.right, maximum)
        return goodNodesMax(root, root.val)
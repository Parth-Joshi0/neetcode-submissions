# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root)[1]
    def depth(self, root):
            if not root:
                return 0, True
            left = self.depth(root.left)
            right = self.depth(root.right)
            return max(left[0], right[0]) + 1, left[1] and right[1] and left[0]-right[0] in (-1, 0, 1)
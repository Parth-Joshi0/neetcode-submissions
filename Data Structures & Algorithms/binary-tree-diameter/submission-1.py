# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.max_diameter_recursive(root)[1]

    def max_diameter_recursive(self, root):
        if not root:
            return 0,0
        left_child = self.max_diameter_recursive(root.left)
        right_child = self.max_diameter_recursive(root.right)

        depth = max(left_child[0], right_child[0]) + 1
        max_area_found = max(right_child[1], left_child[1], left_child[0] + right_child[0])
        return depth, max_area_found
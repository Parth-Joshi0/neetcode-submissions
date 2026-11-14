# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_found = root.val

        def dfs(node):
            nonlocal max_path_found

            if not node:
                return 0

            left_child = max(dfs(node.left), 0)
            right_child = max(dfs(node.right), 0)

            max_path_found = max(
                max_path_found,
                left_child + right_child + node.val
            )

            return node.val + max(left_child, right_child)

        dfs(root)
        return max_path_found


                
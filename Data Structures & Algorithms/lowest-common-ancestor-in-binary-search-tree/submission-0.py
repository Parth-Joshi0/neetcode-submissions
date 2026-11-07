# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == q.val: # They are equal
            return p
        elif p.val == root.val or q.val == root.val: # One of them is a root
            return root
        elif p.val > root.val and q.val > root.val: # both lie on the right side of the root
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val: # both lie on the left side of the root
            return self.lowestCommonAncestor(root.left, p, q)
        else: # Both lie on opposite ends of the root
            return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def inorder_traversal(root):
            if not root:
                return
            inorder_traversal(root.left)
            arr.append(root)
            inorder_traversal(root.right)
        inorder_traversal(root)
        return arr[k-1].val
            

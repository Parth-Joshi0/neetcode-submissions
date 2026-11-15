# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        res = ""
        while queue:
            node = queue.popleft()
            if node:
                res += f'#{node.val}'
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += f'#x'
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '':
            return None
        res = data.split('#')
        queue = deque([TreeNode(res[0])])
        for i in range(1, len(res)-1, 2):
            node = queue.popleft()
            if res[i]:
                node.left = TreeNode(res[i])
                queue.append(node.left)
            if res[i+1]:
                node.right = TreeNode(res[i+1])
                queue.append(node.right)
        return root




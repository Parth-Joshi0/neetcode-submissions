
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        res = [[]]
        nodes_left_in_level = 1
        level = 0

        while queue:
            if nodes_left_in_level == 0:
                nodes_left_in_level = len(queue)
                level += 1
                res.append([])

            root = queue.popleft()
            res[level].append(root.val)

            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

            nodes_left_in_level -= 1

        return res

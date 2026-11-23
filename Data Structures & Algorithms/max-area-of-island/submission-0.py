class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        queue = deque()
        area = 0
        def bfs(row, col):
            queue.append((row, col))
            area = 0
            while queue:
                x, y = queue.pop()
                if x >= len(grid) or x < 0:
                    continue
                if y >= len(grid[0]) or y < 0:
                    continue
                if grid[x][y] != 1:
                    continue
                area += 1
                grid[x][y] = '#'
                queue.append((x+1, y))
                queue.append((x-1, y))
                queue.append((x, y+1))
                queue.append((x, y-1))
            return area


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = max(bfs(row, col), area)
        return area
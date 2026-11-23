from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue = deque()
        islands = 0
        def bfs(row, col):
            queue.append((row, col))
            while queue:
                x, y = queue.pop()
                if x >= len(grid) or x < 0:
                    continue
                if y >= len(grid[0]) or y < 0:
                    continue
                if grid[x][y] != '1':
                    continue
                grid[x][y] = '#'
                queue.append((x+1, y))
                queue.append((x-1, y))
                queue.append((x, y+1))
                queue.append((x, y-1))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    bfs(row, col)
                    islands += 1
        return islands
                
    
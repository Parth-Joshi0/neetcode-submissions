class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        def ray_cast(x, y, direction):
            for i in range(1, n):
                new_x = x + direction[0] * i
                new_y = y + direction[1] * i

                if not (0 <= new_x < n and 0 <= new_y < n):
                    return False

                if board[new_x][new_y] == 'Q':
                    return True

        def square_in_danger(x, y):
            directions = [(-1, 0), (-1, -1), (-1, 1)]
            for direction in directions:
                if ray_cast(x, y, direction):
                    return True
            return False

        def backtrack(row):
            if row == n:
                res.append(["".join(row) for row in board])
                return
            for i in range(n):
                if not square_in_danger(row, i):
                    board[row][i] = 'Q'
                    backtrack(row+1)
                    board[row][i] = '.'
        
        backtrack(0)
        return res

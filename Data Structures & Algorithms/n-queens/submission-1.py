class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        mask = (1 << n) - 1

        def backtrack(row, cols, diag1, diag2):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            available = mask & ~(cols | diag1 | diag2)

            while available:
                bit = available & -available
                available &= available - 1

                col = bit.bit_length() - 1
                board[row][col] = "Q"

                backtrack(
                    row + 1,
                    cols | bit,
                    ((diag1 | bit) << 1) & mask,
                    (diag2 | bit) >> 1
                )

                board[row][col] = "."

        backtrack(0, 0, 0, 0)
        return res
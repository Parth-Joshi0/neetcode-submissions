
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(seen, x, y, index):
            if index == len(word):
                return True

            adjacents = get_adjacent(x, y, len(board), len(board[0]))

            for i, j in adjacents:
                if (i, j) in seen:
                    continue

                if board[i][j] == word[index]:
                    seen.add((i, j))

                    output = backtrack(seen, i, j, index + 1)

                    seen.remove((i, j))

                    if output:
                        return True

            return False

        def get_adjacent(x, y, n, m):
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            ans = []

            for i, j in directions:
                if 0 <= x+i < n and 0 <= y+j < m:
                    ans.append((x+i, y+j))

            return ans

        for x in range(len(board)):
            for y in range(len(board[0])):

                if board[x][y] == word[0]:
                    seen = {(x, y)}

                    if backtrack(seen, x, y, 1):
                        return True

        return False
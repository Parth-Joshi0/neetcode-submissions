class TrieNode:
    def __init__(self):
        self.end = False
        self.chars = [None] * 26

class PrefixTree:
    def __init__(self, words):
        self.root = TrieNode()
        self.curr = self.root
        for word in words:
            self.add_word(word)
    
    def add_word(self, word):
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not curr.chars[i]:
                curr.chars[i] = TrieNode()
            curr = curr.chars[i]
        curr.end = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        matrix = [[False] * len(board[0]) for _ in range(len(board))]
        prefix_tree = PrefixTree(words)
        res = []
        def dfs(pos, curr_node, s):
            x, y = pos
            i = ord(board[x][y]) - ord('a')
            if not curr_node.chars[i]:
                return
            s += board[x][y]
            if curr_node.chars[i].end:
                curr_node.chars[i].end = False
                res.append(s)
            matrix[x][y] = True
            positions = self.getAdjacentPositions(board, matrix, x, y)
            for loc in positions:
                dfs(loc, curr_node.chars[i], s)
            matrix[x][y] = False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs((i, j), prefix_tree.root, "")
        return res
    
    def getAdjacentPositions(self, board, matrix, x, y):
        res = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                pos = (x+i, y+j)
                if abs(i) + abs(j) != 1:
                    continue
                if pos[0] >= len(board) or pos[0] < 0:
                    continue
                if pos[1] >= len(board[0]) or pos[1] < 0:
                    continue
                if not matrix[x+i][y+j]:
                    res.append(pos)
        return res
    
        
                

        
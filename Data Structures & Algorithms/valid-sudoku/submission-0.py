class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colList = [0] * 9
        rowList = [0] * 9
        grdList = [0] * 9

        for row in board:
            for num in row:
                if num != ".":
                    if rowList[int(num) - 1] != 0:
                        return False
                    rowList[int(num) - 1] = num
            rowList = [0] * 9
        

        for col in range(0, 9):
            for row in range(0, 9):
                num = board[row][col]
                if num != ".":
                    if colList[int(num) - 1] != 0:
                        return False
                    colList[int(num) - 1] = num
            colList = [0] * 9
            
        square_check_list = [(1, 1), (4, 1), (7, 1), (1, 4), (4, 4), (7, 4), (1, 7), (4, 7), (7, 7)]
        
        for pair in square_check_list:
            for i in (-1, 0, 1):
                for j in (-1, 0, 1):
                    num = board[pair[0] + i][pair[1] + j]
                    if num != ".":
                        if grdList[int(num) - 1] != 0:
                            return False
                        grdList[int(num) - 1] = num
            grdList = [0] * 9

        return True
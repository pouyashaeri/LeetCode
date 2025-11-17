from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag = True
        # Check rows
        for i in range(9):
            count = {}
            for j in range(9):
                if board[i][j] != ".":
                    count[board[i][j]] = count.get(board[i][j], 0) + 1
            for cnt in list(count.values()):
                if cnt != 1:
                    flag = False

        # Check cols
        for i in range(9):
            count = {}
            for j in range(9):
                if board[j][i] != ".":
                    count[board[j][i]] = count.get(board[j][i], 0) + 1
            for cnt in list(count.values()):
                if cnt != 1:
                    flag = False

        # Check sub-grid
        for k in [0, 3, 6]:
            for m in [0, 3, 6]:
                count = {}
                for i in range(3):          # i = [0, 1, 2]
                    for j in range(3):      # j = [0, 1, 2] 
                        if board[i+k][j+m] != ".":
                            count[board[i+k][j+m]] = count.get(board[i+k][j+m], 0) + 1
                for cnt in list(count.values()):
                    if cnt != 1:
                        flag = False

        return flag
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = []
        for r in range(9):
            for c in range(9):
                if board[c][r] != ".":
                    check.append(board[c][r])
            if len(check)!=len(set(check)):
                return False
            check = []
        
        check = []
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    check.append(board[r][c])
            if len(check)!=len(set(check)):
                return False
            check = []

        check = []
        for r in range(0,9,3):
            for c in range(0,9,3):
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] != ".":
                            check.append(board[r+i][c+j])
                if len(check)!=len(set(check)):
                    return False
                check = []

        return True
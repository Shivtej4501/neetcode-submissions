class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            # checking rows
            l_row = board[i]
            l_row = [x for x in l_row if x != '.']
            s_row = set(l_row)
            if len(l_row) != len(s_row):
                return False
            # checking column
            l_column = []
            for j in range(0,9):
                l_column.append(board[j][i])
            l_column = [x for x in l_column if x != '.']
            s_column = set(l_column)
            if len(l_column) != len(s_column):
                return False
        
        
        # checking 3x3 matrix
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                l = []

                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        l.append(board[i][j])

                l = [x for x in l if x != '.']
                s = set(l)

                if len(l) != len(s):
                    return False
        
        return True
            

            
        
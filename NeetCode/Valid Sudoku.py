class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = {i:set() for i in range(9)}

        #Check rows
        for row in board:
            rows = set()
            for num in row:
                if num not in rows and num.isdigit():
                    rows.add(num)
                elif num in rows:
                    return False

        #Check columns
        for i in range(9):
            cols = set()
            for row in board:
                if row[i] not in cols and row[i].isdigit():
                    cols.add(row[i])
                elif row[i] in cols:
                    return False

        #Check squares
        for y in range(9):
            for x in range(9):
                if board[y][x].isdigit():
                    if board[y][x] not in squares[(x//3)*3+(y//3)]:
                        squares[(x//3)*3+(y//3)].add(board[y][x])
                    else:
                        return False
        return True
    
if __name__ == "__main__":
    
    board =[["1","2",".",".","3",".",".",".","."],
            ["4",".",".","5",".",".",".",".","."],
            [".","9","8",".",".",".",".",".","3"],
            ["5",".",".",".","6",".",".",".","4"],
            [".",".",".","8",".","3",".",".","5"],
            ["7",".",".",".","2",".",".",".","6"],
            [".",".",".",".",".",".","2",".","."],
            [".",".",".","4","1","9",".",".","8"],
            [".",".",".",".","8",".",".","7","9"]]
    
    print(Solution().isValidSudoku(board))


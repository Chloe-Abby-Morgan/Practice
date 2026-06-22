class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def backtrack(x,y,point):
            if point == len(word):
                return True

            if (x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or word[point] != board[x][y] or (x,y) in visited):
                return False
            
            visited.add((x,y))
            res = (backtrack(x+1,y,point+1) or backtrack(x-1,y,point+1) or backtrack(x,y+1,point+1) or backtrack(x,y-1,point+1))
            visited.remove((x,y))

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False
        

            
            
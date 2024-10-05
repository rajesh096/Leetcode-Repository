class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        def res(i,j,k):
            if(k==len(word)):
                return True
            if(i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]!=word[k]):
                return False
            temp = board[i][j]
            board[i][j]='0'
            f=(res(i+1,j,k+1) or
            res(i-1,j,k+1) or
            res(i,j-1,k+1) or
            res(i,j+1,k+1))
            board[i][j]=temp
        
            return f
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]==word[0]) and res(i,j,0):
                    return True
        return False
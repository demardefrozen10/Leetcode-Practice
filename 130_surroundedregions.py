class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        queue = deque()
        visited = set()

        for i in range(rows):
            if board[i][0] == "O":
                queue.appendleft((i,0))
                visited.add((i,0))
            if board[i][cols-1] == "O":
                queue.appendleft((i,cols-1))
                visited.add((i,cols-1))
        
        for j in range(1,cols):
            if board[0][j] == "O":
                queue.appendleft((0,j))
                visited.add((0,j))
            if board[rows-1][j] == "O":
                queue.appendleft((rows-1,j))
                visited.add((rows-1,j))
        while queue:
            row, col = queue.pop()
            neighbors = [(row+1, col), (row-1,col), (row,col-1), (row,col+1)]
            for n_row, n_col in neighbors:
                if n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols and (n_row,n_col) not in visited and board[n_row][n_col] == "O":
                    queue.appendleft((n_row,n_col))
                    visited.add((n_row,n_col))
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"

                

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(row, col):
            # If out of bounds or reached the last column
            if col == n - 1:
                return 0
            if memo[row][col] != -1:
                return memo[row][col]
            
            max_moves = 0
            current_value = grid[row][col]
            
            # List of potential moves
            directions = [(-1, 1), (0, 1), (1, 1)]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] > current_value:
                    max_moves = max(max_moves, 1 + dfs(new_row, new_col))
            
            memo[row][col] = max_moves
            return max_moves
        
        max_result = 0
        # Try to start from each cell in the first column
        for row in range(m):
            max_result = max(max_result, dfs(row, 0))
        
        return max_result
   
class Solution:
    def strangePrinter(self, s: str) -> int:
        
        if not s:
            return 0

        n = len(s)
        
       
        dp = [[0] * n for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                dp[i][j] = dp[i][j - 1] + 1
                
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
        
        return dp[0][n - 1]



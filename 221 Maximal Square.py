class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        max_edge = 0

        for i in range(len(matrix)):
            dp[i][0] = int(matrix[i][0])
            max_edge = max(max_edge, dp[i][0])
        for j in range(len(matrix[0])):
            dp[0][j] = int(matrix[0][j])
            max_edge = max(max_edge, dp[0][j])

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == "1":
                    # 关键是要理解这一行
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_edge = max(max_edge, dp[i][j])

        return max_edge ** 2
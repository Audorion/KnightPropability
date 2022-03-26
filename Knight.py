class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> (float, float):
        if N < 3:
            return 0

        dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1

        for _ in range(K):
            newDp = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < N and 0 <= y < N:
                            newDp[i][j] += dp[x][y] / 8
            dp = newDp
        return sum(map(sum, dp)), dp[0][0]


cls = Solution()
p1, p2 = cls.knightProbability(4, 3, 0, 0)
print(f'Вероятность того что конь останется на доске {p1}')
print(f'Вероятность того что конь вернется в начало {p2}')

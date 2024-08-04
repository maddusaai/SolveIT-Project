class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0]) # dimensions 
        
        @cache
        def fn(i, j):
            """Return number of unique paths arriving at (i, j)."""
            if obstacleGrid[i][j] or i < 0 or j < 0: return 0 
            if i == j == 0: return 1
            return fn(i-1, j) + fn(i, j-1)
        
        return fn(m-1, n-1)

lis = list(int(input()))
sol = Solution()
sol.uniquePathsWithObstacles(lis)
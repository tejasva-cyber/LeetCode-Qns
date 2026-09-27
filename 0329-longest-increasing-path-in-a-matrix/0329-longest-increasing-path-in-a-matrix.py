class Solution(object):
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        
        # 1. Deterministic Manual Memory Allocation (Bypassing lru_cache)
        memo = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            # 2. State-Space Validation: Instantly return if already computed
            if memo[r][c] != 0:
                return memo[r][c]

            best = 1
            
            # 3. Vectorized Directional Mapping
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))

            # Write-back to the memory state table
            memo[r][c] = best
            return best

        longest_path = 0
        
        for r in range(rows):
            for c in range(cols):
                longest_path = max(longest_path, dfs(r, c))

        return longest_path
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n == 1: return 1  # Base case: only one way to tile a 2×1 board
        if n == 2: return 2  # Base case: two ways to tile a 2×2 board
        if n == 0: return 0  # Edge case: no board, no solution
        
        # Initialize dp array with base cases
        dp = [1, 1, 2]  # dp[0]=1 (empty), dp[1]=1, dp[2]=2
        
        # Build up solutions iteratively
        for i in range(3, n+1):
            # Formula: current solution = (solution from 3 steps ago + 2 * solution from 1 step ago) % MOD
            value = (dp[i-3] + 2 * dp[i-1]) % MOD
            dp.append(value)
        
        return dp[-1]  # Return the solution for length n
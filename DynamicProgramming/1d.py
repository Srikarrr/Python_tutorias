import numpy as np

def compute_optimal_cost(path1, path2):
    n = len(path1)
    m = len(path2)

    # DP table to store optimal cost
    dp = np.zeros((n+1, m+1))

    # Initialization
    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, n+1):
        for j in range(1, m+1):
            if path1[i-1] == path2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No cost if they match
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1  # Insert or delete
    
    return dp[n][m]

# Example usage
path1 = [1, 2, 3, 4]
path2 = [2, 3, 4, 5]
cost = compute_optimal_cost(path1, path2)
print(f"Optimal cost: {cost}")

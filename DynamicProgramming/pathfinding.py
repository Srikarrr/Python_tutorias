import numpy as np

def min_path_sum(image):
    """
    Finds the minimum path sum from the top-left corner to the bottom-right corner
    of an image (or matrix) where each cell contains a cost (energy value).
    """
    m, n = image.shape
    dp = np.zeros((m, n))

    # Initialize the starting point
    dp[0][0] = image[0][0]

    # Fill the first column (only down movement possible)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + image[i][0]

    # Fill the first row (only right movement possible)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + image[0][j]

    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + image[i][j]

    return dp[m-1][n-1]

# Example usage with a synthetic "energy" matrix:
image = np.array([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])

result = min_path_sum(image)
print(f"Minimum path sum: {result}")


#Time Complexity:𝑂(𝑚×𝑛) O(m×n), since each cell is visited once.
#Space Complexity: 𝑂(𝑚×𝑛) O(m×n), due to the dp table.
def longest_common_subsequence(S, T):
    # Get lengths of the input strings
    m, n = len(S), len(T)

    # Create a 2D array (table) to store lengths of LCS for substrings
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp array using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the longest common subsequence is in dp[m][n]
    return dp[m][n]

# Read input strings
S = input("Enter the first string: ").strip()
T = input("Enter the second string: ").strip()

# Get the length of the longest common subsequence
lcs_length = longest_common_subsequence(S, T)

# Output the result
print(lcs_length)
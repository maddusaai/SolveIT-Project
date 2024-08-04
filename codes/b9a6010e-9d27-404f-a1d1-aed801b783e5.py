def longest_common_subsequence(S, T):
    m, n = len(S), len(T)
    # Initialize a 2D list with zeros
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def shortest_common_supersequence(S, T):
    lcs_length = longest_common_subsequence(S, T)
    # Calculate the length of the shortest common supersequence
    return len(S) + len(T) - lcs_length


S = input().strip()
T = input().strip()

result = shortest_common_supersequence(S, T)
print(result)
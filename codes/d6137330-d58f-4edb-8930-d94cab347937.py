def longest_palindromic_subsequence(S):
    n = len(S)
    # Create a 2D table to store the length of longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the table
    for length in range(2, n+1): # length of the substring
        for i in range(n - length + 1):
            j = i + length - 1
            if S[i] == S[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


S = input().strip()
print(longest_palindromic_subsequence(S))
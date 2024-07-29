def count_alt_subsequences(N):
    MOD = 1000000007
    # Calculate 2^N using fast exponentiation
    total_subsequences = pow(2, N, MOD)
    # Subtract 1 to exclude the empty subsequence
    alt_subsequences = (total_subsequences - 1) % MOD
    return alt_subsequences

# Read input
N = int(input("Enter the number of students: "))

# Calculate the number of alternate subsequences
result = count_alt_subsequences(N)

# Print the result
print(result)
## 0-minoperations.py
def minOperations(n):
    if n == 1:
        return 0  # No operations needed for one 'H'

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0

# Example usage:
n = 4
result = minOperations(n)
print(f"The fewest number of operations needed to achieve {n} 'H' characters is: {result}")


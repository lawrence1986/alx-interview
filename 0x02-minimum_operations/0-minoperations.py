#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0  # No operations needed for one 'H'

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations

# Example usage:
n = 9
result = minOperations(n)
print(f"The fewest number of operations needed to achieve {n} 'H' characters is: {result}")

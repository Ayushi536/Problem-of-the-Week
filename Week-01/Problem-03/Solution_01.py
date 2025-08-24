import math

def find_gcd_of_list(numbers):
    """
    Compute the GCD of a list of integers using Euclidean Algorithm.

    Args:
    numbers (list[int]): List of n integers.

    Returns:
    int: Greatest common divisor of all numbers in the list.
    """
    n = len(numbers)
    if n == 0:
        return 0  # No numbers to compute GCD
    
    # Initialize result with the first number
    result = numbers[0]

    # Iteratively compute GCD with remaining numbers
    for i in range(1, n):
        result = math.gcd(result, numbers[i])
    
    return result


# Example usage
numbers1 = [42, 56, 14]
numbers2 = [8, 16, 32, 64]

print(find_gcd_of_list(numbers1))  # Output: 14
print(find_gcd_of_list(numbers2))  # Output: 8

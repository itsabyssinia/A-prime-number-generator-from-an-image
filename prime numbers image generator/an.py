import random
import math
from math import isqrt, log

def miller_rabin(n, k=20):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Composite

    return True  # Probably prime

def aks(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r = 2
    while r <= log(n, 2)**2:
        r += 1

    for a in range(2, min(n, r)):
        if math.gcd(a, n) != 1:
            return False
        if pow(a, n, n) != a:
            return False

    for k in range(1, isqrt(n) + 1):
        if (pow(2, n, r) - 1) % n != 0:
            return False

    return True  # Prime

def is_prime(n):
    if miller_rabin(n):
        return aks(n)  # Final check with AKS
    return False  # Composite

def change_digit_to_prime(ascii_art_number):
    # Convert ASCII art to a number string
    number_str = ascii_art_number.strip().replace('\n', '')  # Simplified for this example

    for i in range(len(number_str)):
        original_digit = number_str[i]
        
        for digit in '0123456789':
            if digit != original_digit:
                # Create a new number by changing one digit
                new_number_str = number_str[:i] + digit + number_str[i+1:]
                new_number = int(new_number_str)

                # Check if the new number is prime
                if new_number > 0 and new_number != int(number_str) and is_prime(new_number):
                    return new_number  # Return the first found prime

    # This case is highly unlikely for large numbers, but handle it gracefully
    return "Unexpected result: No prime found by changing one digit."

# Example usage with an ASCII representation of a large number
ascii_art_number = """
1800
"""  # This is a simplified representation; you can replace it with actual ASCII art

result = change_digit_to_prime(ascii_art_number)

print(f"Changed number to prime: {result}" if isinstance(result, int) else result)

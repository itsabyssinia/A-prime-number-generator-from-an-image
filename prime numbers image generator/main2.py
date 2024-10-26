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

def change_to_prime(original_number):
    num_str = str(original_number)
    length = len(num_str)
    
    for i in range(length):
        for digit in '0123456789':
            if digit != num_str[i]:
                # Create a new number by changing one digit
                new_num = num_str[:i] + digit + num_str[i+1:]
                new_num_int = int(new_num)

                # Skip numbers with leading zeros
                if new_num_int > 0 and new_num_int != original_number and is_prime(new_num_int):
                    return new_num_int  # Return the first found prime

    return None  # No prime found by changing one digit

# Example usage with an 800-digit number
large_number = int("1" + "0" * 798 + "7")  # Example of an 800-digit number (10^798 + 7)
result = change_to_prime(large_number)

if result:
    print(f"Changed number to prime: {result}")
else:
    print("No prime found by changing one digit.")

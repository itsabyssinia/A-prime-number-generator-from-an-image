import random
import math
from math import isqrt, log
import cv2
import numpy as np

# Load the image in grayscale
image = cv2.imread('x.jpg', 0)
height, width = image.shape[:2]
ratio = width / height
new_height = int(30 / ratio)
resized = cv2.resize(image, (30, new_height))

m_array = np.array(resized)
ascii_chars = '18'

# Create a string to hold the ASCII art
ascii_art = ""

for i in range(m_array.shape[0]):
    for j in range(m_array.shape[1]):
        index = int(m_array[i, j] / 128)
        if index >= len(ascii_chars):
            index = len(ascii_chars) - 1  # Clamp to the last index
        ascii_art += ascii_chars[index]
    ascii_art += '\n'

# Get filename from user input
filename = input('Enter file name: ')
with open(filename, 'w') as file:
    file.write(ascii_art)  # Write the ASCII art to the file

# Primality Test Functions
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

# Read the number string from the file
with open(filename, 'r') as file:
    ascii_art_number = file.read().strip()

# Change one digit to find a prime
number_str = ascii_art_number.replace('\n', '')

found_prime = False
for i in range(len(number_str)):
    original_digit = number_str[i]
    
    for digit in '0123456789':
        if digit != original_digit:
            # Create a new number by changing one digit
            new_number_str = number_str[:i] + digit + number_str[i+1:]
            new_number = int(new_number_str)

            # Check if the new number is prime
            if new_number > 0 and new_number != int(number_str):
                if miller_rabin(new_number) and aks(new_number):
                    print(f"Changed number to prime: {new_number}")
                    found_prime = True
                    break
    if found_prime:
        break

if not found_prime:
    print("Unexpected result: No prime found by changing one digit.")

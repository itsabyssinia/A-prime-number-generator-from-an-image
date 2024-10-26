import cv2
import numpy as np
import random
from sympy import nextprime

def generate_prime_image(image_path):
    # Load the image in grayscale
    image = cv2.imread('f.jpg', cv2.IMREAD_GRAYSCALE)
    height, width = image.shape[:2]

    # Resize the image for better processing
    resized = cv2.resize(image, (85, int(85 * height / width)))

    # Convert the image to a string of digits
    digits = ''.join(str(pixel // 32) for pixel in resized.flatten())  # Scale to range 0-9

    # Convert string of digits to an integer
    num = int(digits)

    # Randomly modify one pixel to ensure it's not the same
    random_index = random.randint(0, len(digits) - 1)
    new_digit = str((int(digits[random_index]) + 1) % 10)  # Change the digit
    modified_digits = digits[:random_index] + new_digit + digits[random_index + 1:]

    # Convert back to an integer
    modified_num = int(modified_digits)

    # Find the next prime number
    prime_num = nextprime(modified_num)

    return prime_num

def main():
    image_path = 'monalisa.jpg'  # Change this to your image file path
    prime_number = generate_prime_image(image_path)
    print(f"Generated prime number: {prime_number}")

if __name__ == "__main__":
    main()

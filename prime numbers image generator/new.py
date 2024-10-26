import cv2, numpy as np

image = cv2.imread('f.jpg', 0)
height, width = image.shape[:2]
ratio = width / height
new_height = int(85 / ratio)
resized = cv2.resize(image, (85, new_height))

m_array = np.array(resized)
ascii_chars = '18'
ascii_art = ''

for i in range(m_array.shape[0]):
    for j in range(m_array.shape[1]):
        index = int(m_array[i, j] / 128)
        if index >= len(ascii_chars):
            index = len(ascii_chars) - 1  
        ascii_art += (ascii_chars[index])
    ascii_art += '\n'  

filename = input('Enter file name: ')
with open(filename, 'w') as file:
    file.write(ascii_art)  


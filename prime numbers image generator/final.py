import cv2, numpy as np

image = cv2.imread('HappyFish.jpg', 0) 
height, width = image.shape[:2]
ratio = width/height
new_height = int(100/ratio)
resized = cv2.resize(image, (100, new_height))

m_array = np.array(resized)
ascii = '@#&%*+=-:.'

for i in range(m_array.shape[0]):
    for j in range(m_array.shape[1]):
        if m_array[i,j] != 256:
            m_array[i,j] = ord(ascii[int(m_array[i,j]/25.6)])
        else:
            m_array[i,j] = ord(ascii[9])


filename = input('Enter file name: ')
with open(filename, 'w') as file: 
    file.write(f'{m_array}')  


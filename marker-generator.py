import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

img = np.zeros((1024, 1024, 3), np.uint8)
number_of_elements = 30

colors = [(255, 0, 0), (0,0,255), (0,255,0), (255,255,255), (128,128,128)]

while number_of_elements > 0:
    randomX = random.randrange(0, 1024)
    randomY = random.randrange(0, 512)
    #randomWhiteColor = random.randrange(0,255)
    randomColor = random.choice(colors)
    cv2.rectangle(img, (randomX,randomX), (randomY,randomY), randomColor, -1)
    number_of_elements = number_of_elements - 1

#plt.imshow(img)
#plt.show()
cv2.imwrite("01.png", img)

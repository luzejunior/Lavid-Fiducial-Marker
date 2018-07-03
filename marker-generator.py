import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

number_of_images = 50
colors = [(255, 0, 0), (0,0,255), (0,255,0), (255,255,255), (128,128,128), (64,64,64), (128, 0, 0), (64, 0, 0), (0, 128, 0), (0, 64, 0), (0,0,128), (0,0,64)]
shapes = ["circle", "rectangle"]

while number_of_images > 0:
    img = np.zeros((1024, 1024, 3), np.uint8)
    number_of_elements = random.randrange(20,50)
    while number_of_elements > 0:
        randomShape = random.choice(shapes)
        randomX = random.randrange(0, 1024)
        randomY = random.randrange(0, 1024)
        if randomShape == "rectangle":
            #randomWhiteColor = random.randrange(0,255)
            randomColor = random.choice(colors)
            cv2.rectangle(img, (randomX,randomY), (randomY,randomX), randomColor, 15)
        elif randomShape == "circle":
            circleSize = random.randrange(50, 200)
            randomColor = random.choice(colors)
            cv2.circle(img, (randomX, randomY), circleSize, randomColor, 15)
        number_of_elements = number_of_elements - 1
    path = "Markers/mark" + str(number_of_images) + ".png"
    cv2.imwrite(path, img)
    number_of_images = number_of_images - 1

#plt.imshow(img)
#plt.show()
#cv2.imwrite("04.png", img)

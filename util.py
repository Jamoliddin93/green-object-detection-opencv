import numpy as np
import cv2



def get_limits(color):
    c = np.uint8([[color]])  # BGR values
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]  # Get the hue value

    # Define lower and upper limits for green color
    lowerLimit = np.array([hue - 20, 100, 100], dtype=np.uint8)  # Adjusting for variation in green hue
    upperLimit = np.array([hue + 20, 255, 255], dtype=np.uint8)  # Adjusting for variation in green hue

    return lowerLimit, upperLimit

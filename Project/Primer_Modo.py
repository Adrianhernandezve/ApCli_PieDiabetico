# Import packages
import cv2
import imutils
import numpy as np
from   PIL import Image

def segmentation(img1, img2):

    # Adjust the two images (city)
    img1 = np.array(img1)
    img1 = cv2.resize(img1, (160, 360) )
    img2 = np.array(img2)
    img2 = cv2.flip(img2, 1)
    img2 = cv2.resize(img2, (160,360) )

    # Grayscale
    gray1     = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2     = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    gray_img1 = gray1
    gray_img2 = gray2

    # Find the difference between the two images using absdiff
    diff = cv2.absdiff(gray1, gray2)

    # Apply threshold
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Dilation
    # import numpy as np
    # kernel = np.ones((6,6), np.uint16)
    # dilate = cv2.dilate(thresh, kernel, iterations=0)

    # Find contours
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # Loop over each contour
    for contour in contours:
      if cv2.contourArea(contour) > 1000:
        # Calculate bounding box
        x, y, w, h= cv2.boundingRect (contour)
        # Draw rectangle - bounding box
        cv2.rectangle(img1, (x,y), (x+w, y+h), (0,0,255), 2)
        cv2.rectangle(img2, (x,y), (x+w, y+h), (0,0,255), 2)

    # Show final images with differences
    x      = np.zeros((360,10,3), np.uint8)
    
    result_L = img1
    result_L = Image.fromarray(result_L)
    
    result_R = cv2.flip(img2, 1)
    result_R = Image.fromarray(result_R)

    return result_L, result_R

# Import packages
import cv2
import imutils
import numpy as np
from   PIL import Image

def segmen_tacion(img1, img2):

    # Adjust the two images (city)
    img1 = np.array(img1)
    img1 = cv2.resize(img1, (160, 360))
    img2 = np.array(img2)
    img2 = cv2.flip(img2, 1)
    img2 = cv2.resize(img2, (160,360))

    # Register images
    # Inicializar el detector AKAZE
    akaze = cv2.AKAZE_create()

    # Detectar puntos clave y descriptores
    kp1, des1 = akaze.detectAndCompute(img1, None)
    kp2, des2 = akaze.detectAndCompute(img2, None)

    # Usar el matcher BFMatcher para encontrar las coincidencias
    bf      = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(des1, des2, k = 2)

    # Aplicar la relación de Lowe para filtrar coincidencias
    good_matches = []
    
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Verificar si hay suficientes coincidencias buenas
    if len(good_matches) < 4:
        # No se encontraron suficientes coincidencias entre las imágenes para realizar el registro
        img1_reg = img1
    else:
        # Extraer las ubicaciones de los puntos coincidentes
        points1 = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        points2 = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        # Calcular la matriz de homografía
        h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

        # Usar esta matriz para transformar la imagen volteada
        height, width, channels = img2.shape
        img1_reg = cv2.warpPerspective(img1, h, (width, height))


    # Grayscale
    gray1     = cv2.cvtColor(img1_reg, cv2.COLOR_BGR2GRAY)
    gray2     = cv2.cvtColor(img2,     cv2.COLOR_BGR2GRAY)
    gray_img1 = gray1
    gray_img2 = gray2

    # Find the difference between the two images using absdiff
    diff = cv2.absdiff(gray1, gray2)

    # Apply threshold
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Dilation
    kernel = np.ones((6, 6), np.uint16)
    dilate = cv2.dilate(thresh, kernel, iterations = 0)

    # Find contours
    contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    # Loop over each contour
    for contour in contours:
        if cv2.contourArea(contour) > 100 and cv2.contourArea(contour) < 6000 :
            # Calculate bounding box
            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle - bounding box
            cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show final images with differences
    x        = np.zeros((360,10,3), np.uint8)

    # Show final images with differences

    # Encontrar el píxel más brillante (representa la mayor temperatura)
    max_temp_img1 = np.max(gray_img1)
    max_temp_img2 = np.max(gray_img2)

    if max_temp_img1 > max_temp_img2:
        max_tp = 1
    else:
        max_tp = 2

    
    result_L = img1
    result_L = Image.fromarray(result_L)
    
    result_R = cv2.flip(img2, 1)
    result_R = Image.fromarray(result_R)

    return result_L, result_R #, max_tp

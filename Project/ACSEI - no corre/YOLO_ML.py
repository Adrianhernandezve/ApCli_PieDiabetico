import matplotlib.pyplot as plt
import numpy             as np
import ultralytics
import cv2
import os

def YOLO_pie(img):
    from IPython import display

    display.clear_output()
    ultralytics.checks()

    from PIL             import Image          as PilImage
    from IPython.display import display, Image
    from ultralytics     import YOLO

    model = YOLO(f'best.pt')

    # Importación de la imagen
    filename = list(img.keys())[0]

    # Cargar y mostrar la imagen
    image = PilImage.open(filename)

    results = model.predict(source = image, conf = 0.25)

    masks = results.masks.masks.cpu().numpy()

    rgba_img = apply_mask_with_alpha(img, mask)
    # Convertir la imagen RGBA a formato PIL y guardarla
    output_img = PilImage.fromarray(rgba_img, 'RGBA')
    # output_filename = f"masked_image_{i}.png"
    return output_img

def apply_mask_with_alpha(image, mask):
    # Convertir la imagen PIL a un array numpy
    img_np = np.array(image)

    # Asegura que la máscara sea binaria (0 o 1)
    binary_mask = np.where(mask > 0, 255, 0).astype(np.uint8)

    # Verificar si las dimensiones de la imagen y la máscara coinciden
    if img_np.shape[:2] != binary_mask.shape[:2]:
        # Redimensionar la máscara para que coincida con la imagen
        binary_mask = cv2.resize(binary_mask, (img_np.shape[1], img_np.shape[0]))

    # Crear una imagen RGBA con la máscara como canal alfa
    rgba_image = np.concatenate([img_np, binary_mask[:, :, np.newaxis]], axis=-1)

    return rgba_image

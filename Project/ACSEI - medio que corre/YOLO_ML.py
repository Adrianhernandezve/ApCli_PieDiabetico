import ultralytics
import numpy             as np
import cv2
import os

def YOLO_pie(img, model):

    print('???')

    # Importación de la imagen
    # filename = list(img.keys())[0]

    # Cargar y mostrar la imagen
    # imagen = Image.open(filename)

    results = model.predict(source = img, conf = 0.25)

    masks = results.masks.masks.cpu().numpy()

    rgba_img = apply_mask_with_alpha(img, mask)
    # Convertir la imagen RGBA a formato PIL y guardarla
    output_img = Image.fromarray(rgba_img, 'RGBA')
    # output_filename = f"masked_image_{i}.png"
    return output_img

def apply_mask_with_alpha(imagen, mask):
    # Convertir la imagen PIL a un array numpy
    img_np = np.array(imagen)

    # Asegura que la máscara sea binaria (0 o 1)
    binary_mask = np.where(mask > 0, 255, 0).astype(np.uint8)

    # Verificar si las dimensiones de la imagen y la máscara coinciden
    if img_np.shape[:2] != binary_mask.shape[:2]:
        # Redimensionar la máscara para que coincida con la imagen
        binary_mask = cv2.resize(binary_mask, (img_np.shape[1], img_np.shape[0]))

    # Crear una imagen RGBA con la máscara como canal alfa
    rgba_image = np.concatenate([img_np, binary_mask[:, :, np.newaxis]], axis=-1)

    return rgba_image

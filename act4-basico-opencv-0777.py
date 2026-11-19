# Alejandra Rivera Valenzuela NC = 0200
# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
print("-+-+-+-+-+-+Alejandra Rivera Valenzuela NC = 0200-+-+-+-+-+-+-++-")
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
import os  # Para verificar que el archivo exista.
print("-+-+-+-+-Alejandra Rivera Valenzuela NC 0200-+-+-+-+-")

# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES 0200")
nombre_ventana = 'Gpo 3H snoopy_0200 Alejandra Rivera Valenzuela 0200'
ruta_imagen = 'snoopy_0200.jpg'

# Verificamos si el archivo existe en la carpeta desde donde se ejecuta Python
if not os.path.exists(ruta_imagen):
    print(f"Error: No se encuentra '{ruta_imagen}' en la carpeta: {os.getcwd()}")
    sys.exit()

img = cv2.imread(ruta_imagen)  # Lee la imagen .jpg y la guarda en la variable 'img'

if img is None:
    print("Error: No se pudo leer 'snoopy_0200.jpg'. Revisa que el archivo no esté dañado.")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN 0200")
height, width, channels = img.shape
print(f"Dimensiones de la imagen: {width}x{height} píxeles")
print(f"Número de canales de color: {channels}")
print(f"Tipo de dato de la imagen: {img.dtype}")
print(f"Total de datos/píxeles: {img.size}")

# ==============================================================================
# 3. CREAR VENTANA Y VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. CREANDO VENTANA Y MOSTRANDO IMAGEN ORIGINAL 0200")
print("Presiona cualquier tecla sobre la ventana de la imagen para salir...")

cv2.namedWindow(nombre_ventana, cv2.WINDOW_NORMAL)
cv2.resizeWindow(nombre_ventana, 600, 600)
cv2.imshow(nombre_ventana, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES 0200")
pixel_img = img.copy()

y, x = 100, 150
pixel = pixel_img[y, x]
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

pixel_img[y, x] = [0, 0, 255]
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)

ventana_pixel = 'Pixel Modificado Alejandra Rivera Valenzuela 0200'
cv2.namedWindow(ventana_pixel, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_pixel, 600, 600)
cv2.imshow(ventana_pixel, pixel_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI) 0200")
roi_img = img.copy()

roi = roi_img[50:200, 100:300]
cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)

ventana_roi_marcada = 'ROI Marcada Alejandra Rivera Valenzuela 0200'
cv2.namedWindow(ventana_roi_marcada, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_roi_marcada, 600, 600)
cv2.imshow(ventana_roi_marcada, roi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ventana_roi_recorte = 'ROI Extraida Alejandra Rivera Valenzuela 0200'
cv2.namedWindow(ventana_roi_recorte, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_roi_recorte, 400, 300)
cv2.imshow(ventana_roi_recorte, roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES 0200")
b, g, r = cv2.split(img)

cv2.namedWindow('Canal Azul Gris - Alejandra Rivera 0200', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canal Azul Gris - Alejandra Rivera 0200', 400, 400)
cv2.imshow('Canal Azul Gris - Alejandra Rivera 0200', b)

cv2.namedWindow('Canal Verde Gris - Alejandra Rivera 0200', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canal Verde Gris - Alejandra Rivera 0200', 400, 400)
cv2.imshow('Canal Verde Gris - Alejandra Rivera 0200', g)

cv2.namedWindow('Canal Rojo Gris - Alejandra Rivera 0200', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canal Rojo Gris - Alejandra Rivera 0200', 400, 400)
cv2.imshow('Canal Rojo Gris - Alejandra Rivera 0200', r)

cv2.waitKey(0)
cv2.destroyAllWindows()

zeros = np.zeros_like(b)
blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

cv2.namedWindow('Canal Azul Color - Alejandra Rivera 0200', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canal Azul Color - Alejandra Rivera 0200', 400, 400)
cv2.imshow('Canal Azul Color - Alejandra Rivera 0200', blue_img)

cv2.namedWindow('Canal Verde Color - Alejandra Rivera 0200', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canal Verde Color - Alejandra Rivera 0200', 400, 400)
cv2.imshow('Canal Verde Color - Alejandra Rivera 0200', green_img)

cv2.namedWindow('Canal Rojo Color - Alejandra Rivera 0200', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Canal Rojo Color - Alejandra Rivera 0200', 400, 400)
cv2.imshow('Canal Rojo Color - Alejandra Rivera 0200', red_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES 0200")
resized_img = cv2.resize(img, (400, 300))
cv2.imshow('Redimensionada 400x300 - Alejandra Rivera 0200', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

half_size = cv2.resize(img, None, fx=0.5, fy=0.5)
double_size = cv2.resize(img, None, fx=1.5, fy=1.5)

cv2.imshow('Mitad (0.5x) - Alejandra Rivera 0200', half_size)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Ampliada (1.5x) - Alejandra Rivera 0200', double_size)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES 0200")
height, width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height))

ventana_rotada = 'Rotada 45 grados - Alejandra Rivera Valenzuela 0200'
cv2.namedWindow(ventana_rotada, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_rotada, 600, 600)
cv2.imshow(ventana_rotada, rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES 0200")
horizontal_flip = cv2.flip(img, 1)
ventana_h = 'Volteo Horizontal - Alejandra Rivera 0200'
cv2.namedWindow(ventana_h, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_h, 600, 600)
cv2.imshow(ventana_h, horizontal_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

vertical_flip = cv2.flip(img, 0)
ventana_v = 'Volteo Vertical - Alejandra Rivera 0200'
cv2.namedWindow(ventana_v, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_v, 600, 600)
cv2.imshow(ventana_v, vertical_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

both_flip = cv2.flip(img, -1)
ventana_ambos = 'Volteo Ambos Ejes - Alejandra Rivera 0200'
cv2.namedWindow(ventana_ambos, cv2.WINDOW_NORMAL)
cv2.resizeWindow(ventana_ambos, 600, 600)
cv2.imshow(ventana_ambos, both_flip)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE 0200")
nombre_guardado = 'snoopy_rotada_0200.jpg'
result = cv2.imwrite(nombre_guardado, rotated_img)

if result:
    print(f"Imagen rotada guardada exitosamente como '{nombre_guardado}'")
else:
    print("Error: No se pudo guardar la imagen rotada.")

cv2.destroyAllWindows()
print("\n-+-+-+-+-+-+Alejandra Rivera Valenzuela NC = 0200-+-+-+-+-+-+-++-")




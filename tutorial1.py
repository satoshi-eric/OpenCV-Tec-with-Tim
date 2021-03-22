import cv2

img = cv2.imread('./assets/logo.jpg', 1) # passa nome do arquivo e modo

# Passa a imagem a ser redimensionada e uma tupla com os valores do tamanho da imagem em pixels
# Para redimensionar a imagem em escala, ou seja, para diminuirmos pela metade ou colocarmos o dobro,
# passamos a tupla com valores (0, 0) e passamos os parâmetros de 0 a 1 pelos argumentos fx e fy
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5) 

# Passa imagem a ser rotacionada e o sentido a ser rotacionado com as constantes que estão no cv2
# cv2.cv2.ROTATE_180
# cv2.cv2.ROTATE_90_clockwise
# cv2.cv2.ROTATE_180_COUNTERCLOCKWISE
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)


"""
    Modos:
        cv2.IMREAD_COLOR (-1): carrega a cor da imagem. Qualquer transparência será ignorada. Modo padrão do cv2
        cv2.IMREAD_GRAYSCALE (0): carrega a imagem em escala de cinza 
        cv2.IMREAD_UNCHANGED (1): Carrega a imagem com o canal alpha que permite mudar a transparência
"""

cv2.imwrite('new_img.jpg', img) # passa o nome do arquivoo onde salvar a imagem e a imagem do cv2
cv2.imshow('image', img) # passa nome da janela e imagem a ser mostrada
cv2.waitKey(0) # espera por um tempo infinito se o usuário não pressionar nenhuma tecla. Espera por n segundos se outro parâmetro for passado 
cv2.destroyAllWindows()
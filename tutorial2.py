import cv2
import random

# O que o cv2.imread faz é ler a imagem e convertê-la em uma array do numpy para podermos manipularmos 
img = cv2.imread('./assets/logo.jpg', -1)

# Ao printar uma imagem, uma array do numpy será printada
# Podemos printar o tipo de img e nos retprnará o tipo numpy.ndarray 
# Também podemos printar a forma da imagem q nos trará quaantas linhas, colunas e canais a imagem possui

# print(img) # [[[255, 255, 255] ... [255, 255, 255]]]
# print(type(img)) # <class 'numpy.ndarray'>
# print(img.shape) # (995, 1000, 3)

# cv2 usa o padrão BGR (Blue, Green, Red)

# Com essas informações, podemos mudar a imagem do jeito que quisermos apenas alterando a array
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# manipulando imagens
tag = img[350: 500, 360: 640]
img[100: 250, 200: 480] = tag


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
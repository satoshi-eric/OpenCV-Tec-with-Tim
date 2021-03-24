import numpy as np
import cv2

img = cv2.imread('./assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.7, fy=0.7)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # para algoritmos de detecção de cantos, é mais usar escala de cinza

# passa imagem, numero de melhores cantos, qualidade dos cantos(0 à 1) e distãncia euclidiana entre os cantos
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners) # converte floats para ints

for corner in corners:
    x, y = corner.ravel() # tira as listas dentro de listas [[1, 2], [2, 1]] -> [1, 2, 2, 1]
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Chessboard', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
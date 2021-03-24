import numpy as np
import cv2

cap = cv2.VideoCapture(0) # passa identificador da câmera. Também pode passar um arquivo

while True:
    ret, frame = cap.read() # ret indica se o dispositivo está sendo usado por outro software e frame, o frama 
    width = int(cap.get(3)) # pega a propriedade 3 da camera de captura, no caso a largura
    height = int(cap.get(4)) # pega a propriedade 4 da camera de captura, no caso a altura

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # altera padrão de cores. Passa imagem e código do padrão
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # mask: parte de um frame
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # passa imagem e cores entre um espectro de luz. Retorna apenas cores entre esse espectro

    result = cv2.bitwise_and(frame, frame, mask=mask) # compara 2 imagens e mistura elas usando a mask

    # hsv: Hue Saturation and lightness/brightness
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask) # mask mostra apenas cores em preto e branco 

    if cv2.waitKey(1) == ord('q'): # waitKey retorna o valor ASCCI do caractere pressionado e o compara com o valor ASCCI de q retornado por ord
        break

cap.release() # solta os recursos da camera para que outros softwares possam usá-la
cv2.destroyAllWindows()
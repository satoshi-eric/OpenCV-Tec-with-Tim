import numpy as np
import cv2

cap = cv2.VideoCapture(0) # passa identificador da câmera. Também pode passar um arquivo

while True:
    ret, frame = cap.read() # ret indica se o dispositivo está sendo usado por outro software e frame, o frama 
    width = int(cap.get(3)) # pega a propriedade 3 da camera de captura, no caso a largura
    height = int(cap.get(4)) # pega a propriedade 4 da camera de captura, no caso a altura

    # passa imagem, coordenadas de inicio e fim, cor e espessura da linha (-1 para preencher)
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    # passa imagem, centro, raio, cor e espessura (-1 para preencher)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # passa imagem, texto, coordenadas ((0,0) no canto inferior esquerdo diferente das coordenadas anteriores), 
    # fonte, escala da fonte, cor, espessura da linha e tipo de linha (usar LINE_AA)
    img = cv2.putText(img, 'Hello World', (10, height - 10), font, 1, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): # waitKey retorna o valor ASCCI do caractere pressionado e o compara com o valor ASCCI de q retornado por ord
        break

cap.release() # solta os recursos da camera para que outros softwares possam usá-la
cv2.destroyAllWindows()
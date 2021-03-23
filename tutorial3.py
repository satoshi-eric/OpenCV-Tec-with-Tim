import numpy as np
import cv2

cap = cv2.VideoCapture(0) # passa identificador da câmera. Também pode passar um arquivo

while True:
    ret, frame = cap.read() # ret indica se o dispositivo está sendo usado por outro software e frame, o frama 
    width = int(cap.get(3)) # pega a propriedade 3 da camera de captura, no caso a largura
    height = int(cap.get(4)) # pega a propriedade 4 da camera de captura, no caso a altura

    image = np.zeros(frame.shape, np.uint8) # desenha quadro preto
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # pega cada frame e diminui ele pela metade
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): # waitKey retorna o valor ASCCI do caractere pressionado e o compara com o valor ASCCI de q retornado por ord
        break

cap.release() # solta os recursos da camera para que outros softwares possam usá-la
cv2.destroyAllWindows()
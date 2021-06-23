import cv2
'''IMPORTAR UNA IMAGEN
print("Package Imported")

img = cv2.imread("Resources/Jisoo.png")

cv2.imshow("Output",img)
cv2.waitKey(0)

IMPORTAR UN VIDEO
cap = cv2.VideoCapture("Resources/Prueba.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
        
CAPTURAR VIDEO DE CÁMARA'''
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,50)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
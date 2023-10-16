import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
segmetor = SelfiSegmentation()
fpsReader = cvzone.FPS()

listImg = os.listdir("Images")
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
print(len(imgList))

#change the value with how many times we press the button
indexImg = 0

while True:
    success, img = cap.read()
    imgOut = segmetor.removeBG(img, imgList[indexImg], threshold = 0.5)
    img2 = cv2.flip(imgOut, -1)

    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color = (0, 0, 255))
    print(indexImg)

    cv2.imshow("Image Stacked", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('q'):
        break
import cv2
import glob
import os


def show(image):
    img = cv2.imread('../test/' + image)
    detector = cv2.CascadeClassifier(
        '../Haar-Training-Cat/training/cascades/cascade.xml')
    signs = detector.detectMultiScale(img, minSize=(
        80, 40), scaleFactor=1.1, minNeighbors=1)
    if len(signs) > 0:
        for (x, y, w, h) in signs:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('Frame', img)
            cv2.waitKey(1000)
    else:
        print("False")
    cv2.destroyAllWindows()


files = glob.glob('../test/*.jpg')
for i, f in enumerate(files):
    show(os.path.basename(f))

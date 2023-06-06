import cv2
from PIL import Image

image_pass = 'pup.jpg.jpg'

pup_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_pass)

pup_face = pup_face_cascade.detectMultiScale(image)

pup = Image.open(image_pass)
glasses = Image.open('glasses.png.jpg')
pup = pup.convert("RGBA")
glasses = glasses.convert("RGBA")


for (x,y,w,h) in pup_face:
    glasses = glasses.resize((w, int(h/3)))
    pup.paste(glasses, (x, int(y + h / 4)), glasses)
    pup.save("pup_with_glasses.png")
    pup_with_glasses = cv2.imread('pup_with_glasses.png')
    cv2.imshow("Pup_with_glasses.png", pup_with_glasses)
    cv2.waitKey()
# вибачте фото без білого поля не знайшов а окуляри з уроку брати не хочу
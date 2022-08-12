import time
from PIL import Image
import os
import matplotlib.pyplot as plt
import cv2
# a = str(input("Что вы делаете? "))
# if a == str("работаю"):
#     print("Хорошо, продолжай работать, только недолго!")
# elif a == str("не работаю"):
#     img=Image.open('C:\\Users\\sgus2\\Desktop\\Время кисяк\\pic\\1.jpg')
#     img.show()
# else:
#     print("грустно")

pictures = os.listdir('pic')
print(pictures)
pic_box = plt.figure(figsize=(16,4))
for i, picture in enumerate(pictures):
    picture = cv2.imread('pic/' + picture)
    picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
    pic_box.add_subplot(2,5,i+1)
    plt.imshow(picture)
    plt.axis('off')
plt.show()
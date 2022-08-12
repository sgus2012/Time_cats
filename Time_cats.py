import time
from PIL import Image

a = str(input("Что вы делаете? "))
if a == str("работаю"):
    print("Хорошо, продолжай работать, только недолго!")
elif a == str("не работаю"):
    img=Image.open('C:\\Users\\sgus2\\Pictures\\Новая папка\\_20160116_184834.jpg')
    img.show()
else:
    print("грустно")

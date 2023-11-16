from allText import *
from fetures import *

def image_Resizer(img='none'):
    try:
     newWidth=float(input("Enter the new width (px):"))
     newHeight=float(input("Enter the new height (px):"))
    except ValueError:
        print(f"{errorText}Only numbers allowed")
        exit(image_Resizer,img)
    print(img.format)
    img.thumbnail((newWidth,newHeight))
    image_preview(img)
    print_imgInfo("Resized image details",img)
    image_save(img,img.format)


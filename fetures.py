from allText import *
from PIL import Image
import math,random
def image_preview(img):
    wantPreview=input(f"Do you want to preview the new image?{ifYes}:")
    
    if int(wantPreview)==1:
        print(f"-->Please wait for a while....")
        img.show()
        print(f"-->Image previewed Succesfully")
    
def image_save(img,extentionName='JPG'):
    wantSave=input(f"Do you want to save the new image?{ifYes}:")
    if int(wantSave)==1:
        print(f"{outPutstr}Saving...")
        try:
            Image.open(f"newImg.{str(extentionName)}") 
            img.save(f"newImg{str(math.floor(random.random()*100))}.{str(extentionName)}")
            print(f"{outPutstr}saved!")
        except OSError:
            img.save(f"newImg.{str(extentionName)}")
            
     
def print_imgInfo(sizeType,img):
    print(f"{outPutstr}{sizeType}\nFormate:{img.format}",f"Dimention(width,height):{img.size}",f"Mode:{img.mode}",sep="\n")

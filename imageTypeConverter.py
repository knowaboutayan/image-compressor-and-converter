from allText import *
from fetures import *

def image_type_Converter(img="none"):
     types=['PNG', 'JPG', 'GIF', 'WEBP']
     print("\nAvailable new format")
     for i in range(len(types)):
         print(f"{i+1}.{types[i]}")
     try:
      newFormat=int(input('Select format:'))
     except ValueError or IndexError:
        print(f"{errorText}Input is out of range")
        image_type_Converter(img)
     if newFormat-1 in range(len(types)):
         print(f"{outPutstr} Convertion started....")
         
         image_save(img,types[newFormat-1])
        
         
     else:
         print(f"{errorText}Input is out of range")
         image_type_Converter(img)
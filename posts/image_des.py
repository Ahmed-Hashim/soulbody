from PIL import Image
from .download_img import save_image
from .resize_image import resize_img
import os
def design(link,category,post):
    image=Image.open(resize_img(link)).convert("RGBA")
    design=Image.open(f"posts/static/images/layout/{category}.png")
    wdesign=design.size[0]
    hdesign=design.size[1]
    wimage=image.size[0]
    himage=image.size[1]
    if wimage>himage:
        dif=(wimage-himage)/2
        width=wimage-dif
        im = image.crop((dif, 0, width, himage))
        wim=im.size[0]
        him=im.size[1]
        if wim>wdesign:
            resized_img = im.resize((1600,1600))
            wimg=resized_img.size[0]
            himg=resized_img.size[1]
            merge=Image.new("RGBA",(wdesign,hdesign), (255, 255, 255))
            merge.paste(resized_img,(wdesign-wimg,hdesign-wimg),resized_img)
            merge.paste(design,design)
            mergename=link.split('/')[-1]
            name=mergename.split('.')[0]+'.webp'
            location='media/images/designs/'+name
            merge.save(location)
        elif wim<wdesign:
            resized_des = design.resize((int(wim*1.25),int(him*1.25)))
            resized_des.save("newsize.png")
            wdesign=resized_des.size[0]
            hdesign=resized_des.size[1]
            merge=Image.new("RGBA",(wdesign,hdesign))
            merge.paste(im,(wdesign-wim,hdesign-him),im)
            merge.paste(resized_des,resized_des)
            mergename=link.split('/')[-1]
            name=mergename.split('.')[0]+'.webp'
            location='media/images/designs/'+name
            merge.save(location)            
        else:
            resized_img = im.resize((1600,1600))
            wimg=resized_img.size[0]
            himg=resized_img.size[1]
            merge=Image.new("RGBA",(wdesign,hdesign), (255, 255, 255))
            merge.paste(resized_img,(wdesign-wimg,hdesign-wimg),resized_img)
            merge.paste(design,design)
            mergename=link.split('/')[-1]
            name=mergename.split('.')[0]+'.webp'
            location='media/images/designs/'+name
            merge.save(location)
    elif wimage<himage:
        dif=(himage-wimage)/2
        hight=himage-dif
        im = image.crop((0, dif, wimage, hight))
        wim=im.size[0]
        him=im.size[1]
        if wim>wdesign:
            resized_img = im.resize((1600,1600))
            wimg=resized_img.size[0]
            himg=resized_img.size[1]
            merge=Image.new("RGBA",(wdesign,hdesign), (255, 255, 255))
            merge.paste(resized_img,(wdesign-wimg,hdesign-wimg),resized_img)
            merge.paste(design,design)
            mergename=link.split('/')[-1]
            name=mergename.split('.')[0]+'.webp'
            location='media/images/designs/'+name
            merge.save(location)
        elif wim<wdesign:
            resized_des = design.resize((int(wim*1.25),int(him*1.25)))
            resized_des.save("newsize.png")
            wdesign=resized_des.size[0]
            hdesign=resized_des.size[1]
            merge=Image.new("RGBA",(wdesign,hdesign))
            merge.paste(im,(wdesign-wim,hdesign-him),im)
            merge.paste(resized_des,resized_des)
            mergename=link.split('/')[-1]
            name=mergename.split('.')[0]+'.webp'
            location='media/images/designs/'+name
            merge.save(location)
        else:
            resized_img = im.resize((1600,1600))
            wimg=resized_img.size[0]
            himg=resized_img.size[1]
            merge=Image.new("RGBA",(wdesign,hdesign), (255, 255, 255))
            merge.paste(resized_img,(wdesign-wimg,hdesign-wimg),resized_img)
            merge.paste(design,design)  
            mergename=link.split('/')[-1]
            name=mergename.split('.')[0]+'.webp'
            location='media/images/designs/'+name
            merge.save(location)
    else:
        resized_img = image.resize((1600,1600))
        wimg=resized_img.size[0]
        himg=resized_img.size[1]
        merge=Image.new("RGBA",(wdesign,hdesign), (255, 255, 255))
        merge.paste(resized_img,(wdesign-wimg,hdesign-wimg),resized_img)
        merge.paste(design,design)
    mergename=link.split('/')[-1]
    name=mergename.split('.')[0]+".webp"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    location=f'{BASE_DIR}/media/images/designs/'+name
    print(location)
    merge.save(location,format="webp")
    return 


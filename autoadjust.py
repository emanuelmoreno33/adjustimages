from PIL import Image
import os
from datetime import datetime
from tqdm import tqdm


def autoadjust():
    pbar = tqdm(total=100,colour="green")
    cwd = os.getcwd()
    dir_list = [f for f in os.listdir(format(cwd)+"/imagenes") if os.path.isfile(os.path.join(format(cwd)+"/imagenes", f))]
    updatebar = (100/len(dir_list))/2
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    sizes = [
        {"height":150,
        "width":150},
        {"height":300,
        "width":300},
        {"height":1024,
        "width":1024},
        {"height":60,
        "width":60},
        {"height":1080,
        "width":1080},
    ]

    for img in dir_list:
        try:
            imgsplit = img.split(".")
            folderpath = format(cwd)+"/imagenes/"+dt_string+"_"+imgsplit[0]
            isExist = os.path.exists(folderpath)
            if not isExist:
                os.makedirs(folderpath)
                os.makedirs(folderpath+"/ad")
                os.makedirs(folderpath+"/tb")

            for size in sizes:
                image = Image.open(format(cwd)+"/imagenes/"+img)
                image.thumbnail((size['height'], size['width']))
                image.save(folderpath+"/tb/"+str(size['width'])+'_'+img)
            pbar.update(updatebar)
            
            for size in sizes:
                image = Image.open(format(cwd)+"/imagenes/"+img)
                new_image = image.resize((size['height'], size['width']))
                new_image.save(folderpath+"/ad/"+str(size['width'])+'_'+img)
            pbar.update(updatebar)

        except Exception as ex:
            print(ex)
            pass
    pbar.close()

autoadjust()

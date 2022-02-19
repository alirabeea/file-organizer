import os
import shutil
from time import sleep

os.chdir('DIRECTORYNAME') 
curFolder = os.getcwd()

image_formats = ["jpg","png","jpeg","tiff","tif","bmp","eps","webp","heic"]
video_formats = ["webm","mkv","flv","vob","ogv","ogg","gif","drc","gifv","mng","avi","mp4"]
audio_formats=["mp3","wav"]
document_formats=["ai","ait","txt","rtf","pdf","doc","docx","pptx"]
developer_formats=["py","js","css","html","java","c","h"]
misc_formats=["zip","dmg"]


if not os.path.isdir(os.path.join(curFolder,"Images")):
    os.mkdir(os.path.join(curFolder,"Images"))
if not os.path.isdir(os.path.join(curFolder,"Videos")):
    os.mkdir(os.path.join(curFolder,"Videos"))
if not os.path.isdir(os.path.join(curFolder,"Audio")):
    os.mkdir(os.path.join(curFolder,"Audio"))
if not os.path.isdir(os.path.join(curFolder,"Docs")):
    os.mkdir(os.path.join(curFolder,"Docs"))
if not os.path.isdir(os.path.join(curFolder,"Dev")):
    os.mkdir(os.path.join(curFolder,"Dev"))
if not os.path.isdir(os.path.join(curFolder,"Packages")):
    os.mkdir(os.path.join(curFolder,"Packages"))
if not os.path.isdir(os.path.join(curFolder,"Misc")):
    os.mkdir(os.path.join(curFolder,"Misc"))

while True: 
    files = os.listdir(curFolder)

    for file in files:
        if os.path.isfile(file):
            ext = file.split(".")[-1].lower()

            if ext in image_formats:
                shutil.move(file,"./Images/"+file)
            elif ext in video_formats:
                shutil.move(file,"./Videos/"+file)
            elif ext in audio_formats:
                shutil.move(file,"./Audio/"+file)
            elif ext in document_formats:
                shutil.move(file,"./Docs/"+file)
            elif ext in developer_formats:
                shutil.move(file,"./Dev/"+file)
            elif ext in misc_formats:
                shutil.move(file,"./Packages/"+file)
            else:
                shutil.move(file,"./Misc/"+file)
    del files
    sleep(10)

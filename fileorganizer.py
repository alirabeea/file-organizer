import os
import shutil
from time import sleep
from decouple import config

DIRECTORYPATH = config('DIRECTORYPATH')
os.chdir(DIRECTORYPATH) 
curFolder = os.getcwd()
TARGETPATH = config('TARGETPATH')
os.chdir(TARGETPATH) 
targetFolder = os.getcwd()

image_formats = ["jpg","png","jpeg","tiff","tif","bmp","eps","webp","heic"]
video_formats = ["webm","mkv","flv","vob","ogv","ogg","gif","drc","gifv","mng","avi","mp4"]
audio_formats=["mp3","wav"]
document_formats=["ai","ait","txt","rtf","pdf","doc","docx","pptx"]
developer_formats=["py","js","css","html","java","c","h"]
misc_formats=["zip","dmg"]


if not os.path.isdir(os.path.join(targetFolder,"Images")):
    os.mkdir(os.path.join(targetFolder,"Images"))
if not os.path.isdir(os.path.join(targetFolder,"Videos")):
    os.mkdir(os.path.join(targetFolder,"Videos"))
if not os.path.isdir(os.path.join(targetFolder,"Audio")):
    os.mkdir(os.path.join(targetFolder,"Audio"))
if not os.path.isdir(os.path.join(targetFolder,"Docs")):
    os.mkdir(os.path.join(targetFolder,"Docs"))
if not os.path.isdir(os.path.join(targetFolder,"Dev")):
    os.mkdir(os.path.join(targetFolder,"Dev"))
if not os.path.isdir(os.path.join(targetFolder,"Packages")):
    os.mkdir(os.path.join(targetFolder,"Packages"))
if not os.path.isdir(os.path.join(targetFolder,"Misc")):
    os.mkdir(os.path.join(targetFolder,"Misc"))

os.chdir(DIRECTORYPATH)

while True: 
    files = os.listdir(curFolder)
    print(files)
    for file in files:
        if os.path.isfile(file):
            ext = file.split(".")[-1].lower()
            print(file, ext)
            if ext in image_formats:
                shutil.move(file,targetFolder+"/Images/"+file)
            elif ext in video_formats:
                shutil.move(file,targetFolder+"/Videos/"+file)
            elif ext in audio_formats:
                shutil.move(file,targetFolder+"/Audio/"+file)
            elif ext in document_formats:
                shutil.move(file,targetFolder+"/Docs/"+file)
            elif ext in developer_formats:
                shutil.move(file,targetFolder+"/Dev/"+file)
            elif ext in misc_formats:
                shutil.move(file,targetFolder+"/Packages/"+file)
            else:
                shutil.move(file,targetFolder+"/Misc/"+file)
    del files
    sleep(15)

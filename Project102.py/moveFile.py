import os
import shutil
import sys
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:/Users/kovai/Downloads"
to_dir="C:/Users/kovai/OneDrive/Desktop/code/Python/Project102.py"

isExist=os.path.exists(from_dir)
list_of_files = os.listdir(from_dir)
print(list_of_files)
print(isExist)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"{event.src_path} has been created")

    def on_deleted(self, event):
        print(f"{event.src_path} has been created")

    def on_modified(self, event):
        print(f"{event.src_path} has been modified")

    def on_moved(self, event):
        print(f"{event.src_path} has been moved")


for fileName in list_of_files:
        name, extension=os.path.splitext(fileName)
        print(name)
        print(extension)
        if extension=="":
            continue
        if extension in [".gif",".png","jpg",".jpeg",".jfif"]:
            path1=from_dir+"/"+fileName
            path2=to_dir+'/'+ "Image_files"
            path3=path2+"/"+fileName
            if os.path.exists(path2):
                shutil.copy(path1,path3)
            else: 
                os.makedirs(path2)
                shutil.copy(path1,path3)
        if extension in [".pdf", ".txt", ".docx"]:
            path1=from_dir+"/"+fileName
            path2=to_dir+'/'+ "Doc_files"
            path3=path2+"/"+fileName
            if os.path.exists(path2):
                shutil.copy(path1,path3)
            else: 
                os.makedirs(path2)
                shutil.copy(path1,path3)

event_handler=FileEventHandler()
observer=Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()
try:

    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
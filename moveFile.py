import os
import shutil

from_dir = "C:/Users/lenovo/Downloads"
to_dir = "C:/Users/lenovo/OneDrive/Desktop/sample doc"
file_list = os.listdir("C:/Users/lenovo/Downloads")
# print(file_list) #

for i in file_list:
    root,ext =  os.path.splitext(i)
    print("FILE NAME:",root)
    print("FILE EXTENSION:",ext)


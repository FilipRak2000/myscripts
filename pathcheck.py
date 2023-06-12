#!/usr/bin/python3

import os 
path = str(input("path name:"))

if os.path.isdir(path):
    print("it is dir")
elif os.path.isfile(path):
    print("it is file!")
else:
    print("file or dir doesnt exists")  

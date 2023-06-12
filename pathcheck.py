import os 
path = str(input("Podaj nazwe sciezki:"))

if os.path.isdir(path):
    print("its dir")
elif os.path.isfile(path):
    print("file!")
else:
    print("nothing")        
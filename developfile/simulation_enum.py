import os

path = "public/simulations"
files = os.listdir(path)
for file in files:
    print(file)

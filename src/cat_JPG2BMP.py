import glob
import PIL
from PIL import Image
import os

files = glob.glob('../cat/*.jpg')

for i, f in enumerate(files):
    img = Image.open(f)
    newName = f.replace('resize', 'bmp')
    newName = newName.replace('.jpg', '.bmp')
    img.save(newName)
    os.remove(f)

import PIL
from PIL import Image
import glob
import os
import shutil
from time import sleep


def emptydir(dirpath):
    if os.path.isdir('../' + dirpath):
        shutil.rmtree('../' + dirpath)
        sleep(2)
    os.mkdir('../' + dirpath)


def dirResize(src, dst):
    emptydir(dst)
    files = glob.glob('../' + src + '/*jpg')
    for i, f in enumerate(files):
        img = Image.open(f)
        img_new = img.resize((300, 250), PIL.Image.ANTIALIAS)
        outname = 'resizejpg' + '{:0>3d}'.format(i+1) + '.jpg'
        img_new.save('../' + dst + '/' + outname)


dirResize('cat_sr', 'cat')
dirResize('test_sr', 'test')

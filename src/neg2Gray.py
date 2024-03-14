import glob
import PIL
from PIL import Image
import os
import shutil
from time import sleep


def emptydir(dirpath):
    if os.path.isdir('../' + dirpath):
        shutil.rmtree('../' + dirpath)
        sleep(2)
    os.mkdir('../' + dirpath)


def dirNeg2Gray(src, dst):
    emptydir(dst)
    files = glob.glob('../' + src + '/*jpg')
    for i, f in enumerate(files):
        img = Image.open(f)
        img_new = img.resize((500, 350), PIL.Image.ANTIALIAS)
        newName = 'Gray' + '{:0>3d}'.format(i+1) + '.jpg'
        img_new = img_new.convert('L')
        img_new.save('../' + dst + '/' + newName)


dirNeg2Gray('neg_sr', 'neg')

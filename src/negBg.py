import PIL
import glob
import os

fp = open('../Haar-Training-cat/training/negative/bg.txt', 'w')

fp.write("")

files = glob.glob('../Haar-Training-cat/training/negative/*.jpg')

text = ''

for file in files:
    basename = os.path.basename(file)
    filename = 'negative/' + basename
    text += filename + '\n'

fp.write(text)
fp.close()

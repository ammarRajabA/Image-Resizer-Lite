import PIL
from PIL import Image
import sys
import os

percentage=25

for i in range(1,len(sys.argv)):
	img=Image.open(sys.argv[i])
	new_size=(int((int(percentage)/100.0)*img.size[0]),int((int(percentage)/100.0)*img.size[1]))
	print "Resizing from "+str(img.size)+" to "+str(new_size)
	img2=img.resize(new_size,PIL.Image.ANTIALIAS)
	img2.save(sys.argv[i].split(".")[0]+"_resized."+sys.argv[i].split(".")[1])
	print "Done...!"

	
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxA
MessageBox(None, 'Programmed by Ammar Rajab :) ', 'Done', 0)
	

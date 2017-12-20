from generate_cmap import generate_cmap_file
import cv2
import numpy as np
import os
from generate_bitmap import generateLetterBitmap
import glob
import ast
from __future__ import unicode_literals

generate_cmap_file("../Fonts/ml")

os.mkdir("Letters")
f = open("character_map.txt", 'r')
list_map = f.readlines()
count_char = {}
for element in list_map:
	if(element[0] == '['):
		cmap = ast.literal_eval(element)
		for unicode_char in cmap:
			if(os.path.isdir("Letters/"+unicode_char) == False):
				os.mkdir("Letters/"+unicode_char)
				count_char[unicode_char] = 0
			else:
				count_char[unicode_char] += 1
			s = '"\u" + ("0"*(4 - len(unicode_char))) + unicode_char'
			print ("Character to be encoded : ", s)
			#img = generateLetterBitmap(font_name, s, 64*64)
			#cv2.imwrite("Letters/"+unicode_char+"/Image_"+count_char[unicode_char]+".jpg")
	else:
		print ("Font Name : ", element)
		font_name = element





#from generate_cmap import generate_cmap_file
import cv2
import numpy as np
import os
from generate_bitmap import generateLetterBitmap
import glob
import ast

print ("Creating folder Letters")
if(os.path.isdir("Letters") == False):
	os.mkdir("Letters")
f = open("character_map.txt", 'r')
list_map = f.readlines()
count_char = {}
for element in list_map:
	if(element[0] == '['):
		cmap = ast.literal_eval(element)
		for unicode_char in cmap:
			print ("The path provided to the font is ", font_name)
			if(os.path.isdir("Letters/"+unicode_char) == False):
				os.mkdir("Letters/"+unicode_char)
			if(unicode_char not in count_char.keys()):
				count_char[unicode_char] = 0
			else:
				count_char[unicode_char] = count_char[unicode_char] + 1
			print ("Character to be encoded : ", chr(int(unicode_char, 16)))
			img = generateLetterBitmap(font_name, chr(int(unicode_char, 16)), 64*64)
			cv2.imwrite("Letters/"+unicode_char+"/Image_"+count_char[unicode_char]+".jpg")
	else:
		print ("Font Name : ", element)
		font_name = element





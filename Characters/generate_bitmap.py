# -*- coding: utf-8 -*-

import freetype
import numpy as np
import cv2


def generateLetterBitmap(font_path,character,size=32*32):
	fontface = freetype.Face(font_path)
	fontface.set_char_size(size)
	fontface.load_char(character)
	print ("Printing the type of fontface", type(fontface))

	bitmap = fontface.glyph.outline
	img = np.array(bitmap.points)
	img = 255-img

	return img


# # Test
#font_path = 'Fonts/ml/JACOB.TTF'
#character = 'അ'
#size = 100*100
#img = generateLetterBitmap(font_path,character,size)
#cv2.imwrite('out.jpg',img)


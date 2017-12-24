# -*- coding: utf-8 -*-

import freetype
import numpy as np
import cv2


def generateLetterBitmap(font_path,character,size=32*32):
	fontface = freetype.Face(font_path)
	fontface.set_char_size(size)
	fontface.load_char(character)

	bitmap = fontface.glyph.bitmap
	img = np.array(bitmap.buffer,dtype=np.int32)
	img = img.reshape(bitmap.rows,bitmap.width)
	img = 255-img

	return img


# # Test
#font_path = 'Fonts/ml/Rachana.ttf'
#character = chr(3333)
#size = 100*100
#img = generateLetterBitmap(font_path,character,size)
#cv2.imwrite('out.jpg',img)

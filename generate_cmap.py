import glob
from Naked.toolshed.shell import execute_rb

def generate_cmap_file(folder_name = ""):
	for font_name in glob.glob(folder_name+"/*.ttf"):
		execute_rb('cmap.rb', arguments = font_name)
	for font_name in glob.glob(folder_name+"/*.TTF"):
		execute_rb('cmap.rb', arguments = font_name)

generate_cmap_file("Fonts/ml")

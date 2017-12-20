require 'ttfunk'

file = TTFunk::File.open(ARGV[0])
cmap = file.cmap

chars = {}
unicode_chars = []

cmap.tables.each do |subtable|
  next if !subtable.unicode?
  chars = chars.merge( subtable.code_map )
end

unicode_chars = chars.keys.map{ |dec| dec.to_s(16) }

open('character_map.txt', 'a'){ |f|
	f << ARGV[0] << "\n"
	f << unicode_chars << "\n"
}

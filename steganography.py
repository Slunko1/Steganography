def hide(image, ot_bin):
	if image is None: raise ValueError("Image cannot be None")

	w = image.width
	h = image.height
	index = 0
	for x in range(w):
		for y in range(h):
			binary_string = ""
			pixel = image.getpixel((x, y))

			for color in pixel:
				binary = format(color, '08b')

				if index < len(ot_bin):
					binary_string += binary[:-1] + ot_bin[index]  + ","
					index += 1
				else:
					binary_string += binary + ","

			if binary_string[-1] == ",":
				binary_string = binary_string[:-1]

			r, g, b = binary_string.split(",")

			r, g, b = int(r, 2), int(g, 2), int(b, 2)

			image.putpixel((x, y), (r, g, b))

	return image, index

def convert_ot_to_binary(ot):
	if ot is None: raise ValueError("OT cannot be None")
	binary = ""
	for char in ot:
		binary += format(ord(char), '08b')

	return binary
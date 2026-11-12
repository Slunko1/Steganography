from PIL import Image

def load_image(path):
	image = Image.open(path)
	image = image.convert("RGB")

	return image

def hide(image, ot_bin):
	if image is None: raise ValueError("Image cannot be None")

	w = image.width
	h = image.height
	index = 0

	for x in range(w):
		for y in range(h):
			pixel = image.getpixel((x, y))
			r, g, b = pixel

			for color in pixel:
				binary = bin(ord(color))

				if index >= len(ot_bin):
					binary[-1] = ot_bin[index]
					index += 1
				else:
					return

def convert_ot_to_binary(ot):
	if ot is None: raise ValueError("OT cannot be None")
	binary = ""
	for char in ot:
		binary += format(ord(char), '08b')

	return binary


image = load_image("mercedser.jpg")

print(image.size)
print(image.width)
print(image.height)

ot = "Ahoj"


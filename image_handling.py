from PIL import Image



def load_image(path):
	image = Image.open(path)
	image = image.convert("RGB")

	return image

def save_image(image):
	if image is None: raise ValueError("Image cannot be None")
	image.save("output/encoded.png")

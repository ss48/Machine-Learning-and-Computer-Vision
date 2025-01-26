from PIL import ImageFilter, Image, ImageDraw, ImageFont
filename = "dot_and_hole.jpg"

with Image.open(filename) as img:
    img.load()


for _ in range(10):
    img = img.filter(ImageFilter.MinFilter(3))


img.show()

for _ in range(10):
    img = img.filter(ImageFilter.MaxFilter(3))


img.show()
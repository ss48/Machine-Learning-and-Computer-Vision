from PIL import Image
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.load()


type(img)


isinstance(img, Image.Image)
#img.show()
img.format
print("img-format:" , img.format)

img.size
print("img-size:" , img.size)

img.mode
print("img-mode:", img.mode)
cropped_img = img.crop((300, 150, 700, 1000))
cropped_img.size


cropped_img.show()

#low_res_img = cropped_img.resize(
#    (cropped_img.width // 4, cropped_img.height // 4)
#)
low_res_img = cropped_img.reduce(4)
low_res_img.show()
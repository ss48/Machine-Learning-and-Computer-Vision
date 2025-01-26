
from PIL import ImageFilter, Image, ImageDraw, ImageFont
# Load the image
filename_cat = "cat.jpg"
with Image.open(filename_cat) as img_cat:
    img_cat.load()

# Crop the image
img_cat = img_cat.crop((420, 0, 950, 881))

# Convert to grayscale and apply thresholding
img_cat_gray = img_cat.convert("L")
threshold = 100
img_cat_threshold = img_cat_gray.point(
    lambda x: 255 if x > threshold else 0
)

# Split color channels
if img_cat.mode == "RGBA":
    red, green, blue, alpha = img_cat.split()
elif img_cat.mode == "RGB":
    red, green, blue = img_cat.split()
else:
    raise ValueError(f"Unsupported image mode: {img_cat.mode}")

# Create two canvases
width, height = img_cat.size
canvas1 = Image.new("RGB", (width * 3, height))  # For original, grayscale, thresholded
canvas2 = Image.new("RGB", (width * 3, height))  # For red, green, blue channels

# Paste images onto the canvases
canvas1.paste(img_cat, (0, 0))
canvas1.paste(img_cat_gray.convert("RGB"), (width, 0))  # Grayscale in RGB mode
canvas1.paste(img_cat_threshold.convert("RGB"), (width * 2, 0))  # Thresholded in RGB mode

canvas2.paste(red.convert("RGB"), (0, 0))
canvas2.paste(green.convert("RGB"), (width, 0))
canvas2.paste(blue.convert("RGB"), (width * 2, 0))

# Add labels
def add_labels(canvas, labels, image_width, font_size=20):
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    for i, label in enumerate(labels):
        x = i * image_width + 10  # Adjust label position
        y = 10  # Top margin
        draw.text((x, y), label, fill="white", font=font)


# Add labels to the canvases
add_labels(canvas1, ["Original", "Grayscale", "Thresholded"], width)
add_labels(canvas2, ["Red Channel", "Green Channel", "Blue Channel"], width)

# Show the canvases
canvas1.show()
canvas2.show()

# Optionally save the canvases
canvas1.save("canvas1_labeled.jpg")
canvas2.save("canvas2_labeled.jpg")
threshold = 57
img_cat_threshold = blue.point(lambda x: 255 if x > threshold else 0)
img_cat_threshold = img_cat_threshold.convert("1")
img_cat_threshold.show()
def erode(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MinFilter(3))
    return image


def dilate(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MaxFilter(3))
    return image
#You can use the image processing techniques called erosion and 
# dilation to create a better mask that represents the cat
step_1 = erode(12, img_cat_threshold)
step_1.show()
step_2 = dilate(58, step_1)
step_2.show()
cat_mask = erode(45, step_2)
cat_mask.show()
cat_mask = cat_mask.convert("L")
cat_mask = cat_mask.filter(ImageFilter.BoxBlur(20))
cat_mask.show()
blank = img_cat.point(lambda _: 0)
cat_segmented = Image.composite(img_cat, blank, cat_mask)
cat_segmented.show()
filename_monastery = "monastery.jpg"
with Image.open(filename_monastery) as img_monastery:
    img_monastery.load()

img_monastery.paste(
    img_cat.resize((img_cat.width // 5, img_cat.height // 5)),
    (1300, 750),
    cat_mask.resize((cat_mask.width // 5, cat_mask.height // 5)),
)

img_monastery.show()
logo = "aru.jpg"
with Image.open(logo) as img_logo:
    img_logo.load()


img_logo = Image.open(logo)
img_logo.show()

img_logo = img_logo.convert("L")
threshold = 50
img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
img_logo = img_logo.resize(
    (img_logo.width // 2, img_logo.height // 2)
)
img_logo = img_logo.filter(ImageFilter.CONTOUR)
img_logo.show()

img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
img_logo.show()
img_monastery.paste(img_logo, (180, 160), img_logo)
img_monastery.show()
from PIL import Image, ImageFilter

# Load the image
filename = "building2.png"
with Image.open(filename) as img:
    img.load()

# Apply filters
blur_img = img.filter(ImageFilter.BLUR)
box_blur_5_img = img.filter(ImageFilter.BoxBlur(5))
box_blur_20_img = img.filter(ImageFilter.BoxBlur(20))
gaussian_blur_img = img.filter(ImageFilter.GaussianBlur(20))
sharp_img = img.filter(ImageFilter.SHARPEN)
smooth_img = img.filter(ImageFilter.SMOOTH)

# Define a larger and more interesting crop box
crop_box = (600, 300, 900, 600)  # (left, top, right, bottom)  # Adjusted crop box for more detail

# Crop the images
original_crop = img.crop(crop_box)
blur_crop = blur_img.crop(crop_box)
box_blur_5_crop = box_blur_5_img.crop(crop_box)
box_blur_20_crop = box_blur_20_img.crop(crop_box)
gaussian_blur_crop = gaussian_blur_img.crop(crop_box)
sharp_crop = sharp_img.crop(crop_box)
smooth_crop = smooth_img.crop(crop_box)

# Combine cropped images into a single canvas
width, height = original_crop.size
canvas_width = width * 4  # 4 columns
canvas_height = height * 2  # 2 rows
canvas = Image.new("RGB", (canvas_width, canvas_height))

# Paste images onto the canvas
canvas.paste(original_crop, (0, 0))
canvas.paste(blur_crop, (width, 0))
canvas.paste(box_blur_5_crop, (width * 2, 0))
canvas.paste(box_blur_20_crop, (width * 3, 0))
canvas.paste(gaussian_blur_crop, (0, height))
canvas.paste(sharp_crop, (width, height))
canvas.paste(smooth_crop, (width * 2, height))

# Add annotations (optional)
from PIL import ImageDraw, ImageFont

draw = ImageDraw.Draw(canvas)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

draw.text((10, 10), "Original", fill="white", font=font)
draw.text((width + 10, 10), "Blur", fill="white", font=font)
draw.text((width * 2 + 10, 10), "Box Blur 5", fill="white", font=font)
draw.text((width * 3 + 10, 10), "Box Blur 20", fill="white", font=font)
draw.text((10, height + 10), "Gaussian Blur", fill="white", font=font)
draw.text((width + 10, height + 10), "Sharpen", fill="white", font=font)
draw.text((width * 2 + 10, height + 10), "Smooth", fill="white", font=font)

# Show the combined canvas
canvas.show()

# Optionally save the combined canvas
canvas.save("filtered_cropped_images_fixed.png")

img_gray = img.convert("L")
edges = img_gray.filter(ImageFilter.FIND_EDGES)
img_gray.show()
edges.show()

img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH)
edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
edges_smooth.show()

edge_enhance = img_gray_smooth.filter(ImageFilter.EDGE_ENHANCE)
edge_enhance.show()

emboss = img_gray_smooth.filter(ImageFilter.EMBOSS)
emboss.show()